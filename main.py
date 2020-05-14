# -*- coding:utf-8 -*-
import sys, os, multiprocessing, subprocess, signal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMessageBox, QSystemTrayIcon, QMenu, qApp, QAction, QDesktopWidget, QWidget
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QVBoxLayout

from PyQt5 import QtCore
from PyQt5.QtCore import QThread


class Thread(QThread):
    def __init__(self):
        super(Thread, self).__init__()

    def run(self):
        # self._signal.emit()
        # self.trigger.emit("v2ray")
        os.system(
            "/Applications/coggom.app/Contents/Resources/v2ray/v2ray /Applications/coggom.app/Contents/Resources/config.json"
        )


class SystemTray(object):
    # 程序托盘类
    def __init__(self, w):
        self.app = app
        self.thread = Thread()
        self.w = w
        QApplication.setQuitOnLastWindowClosed(
            False)  # 禁止默认的closed方法，只能使用qapp.quit()的方法退出程序
        self.w.hide()  # 不设置显示则为启动最小化到托盘
        self.tp = QSystemTrayIcon(self.w)
        self.initUI()
        self.run()

    def kill_v2ray_process(self, name="v2ray"):
        child = subprocess.Popen(["pgrep", "-f", name],
                                 stdout=subprocess.PIPE,
                                 shell=False)
        pid = int(child.communicate()[0])
        os.kill(pid, signal.SIGKILL)

    def initUI(self):
        # 设置托盘图标

        self.tp.setIcon(QIcon('icons.ico'))

    def quitApp(self):
        # 退出程序
        # self.w.show()  # w.hide() #设置退出时是否显示主窗口
        # re = QMessageBox.question(self.w, "Notification", "Quit ?",
        #                           QMessageBox.Yes | QMessageBox.No,
        #                           QMessageBox.No)
        # if re == QMessageBox.Yes:
        self.tp.setVisible(False)  # 隐藏托盘控件，托盘图标刷新不及时，提前隐藏
        # self.thread.quit()
        self.kill_v2ray_process()

        qApp.quit()  # 退出程序

    def message(self):
        # 提示信息被点击方法
        print("弹出的信息被点击了")

    def act(self, reason):
        # 主界面显示方法
        # 鼠标点击icon传递的信号会带有一个整形的值，1是表示单击右键，2是双击，3是单击左键，4是用鼠标中键点击
        if reason == 2 or reason == 3:
            self.w.show()

    def run(self):

        a1 = QAction('&显示(Show)', triggered=self.w.show)
        a2 = QAction('&退出(Exit)', triggered=self.quitApp)

        self.thread.start()
        # self.thread.trigger.connect("v2ray")
        #self.thread.quit()
        # self.thread.started()

        tpMenu = QMenu()

        tpMenu.addAction(a1)
        tpMenu.addAction(a2)
        self.tp.setContextMenu(tpMenu)
        self.tp.show()  # 不调用show不会显示系统托盘消息，图标隐藏无法调用

        # 信息提示
        # 参数1：标题
        # 参数2：内容
        # 参数3：图标（0没有图标 1信息图标 2警告图标 3错误图标），0还是有一个小图标
        # self.tp.showMessage('Hello', '我藏好了', icon=0)
        # 绑定提醒信息点击事件
        # self.tp.messageClicked.connect(self.message)
        # 绑定托盘菜单点击事件
        self.tp.activated.connect(self.act)
        sys.exit(self.app.exec_())  # 持续对app的连接


class Window(QDockWidget):
    # 主窗口类
    def __init__(self):
        # move()方法移动了窗口到屏幕坐标x=300, y=300的位置.

        super(Window, self).__init__()
        self.initUI()

    def initUI(self):

        self.setWindowFlags(QtCore.Qt.WindowTitleHint
                            | QtCore.Qt.WindowSystemMenuHint
                            | QtCore.Qt.MacWindowToolBarButtonHint
                            | QtCore.Qt.CustomizeWindowHint
                            | QtCore.Qt.FramelessWindowHint)

        self.removeDockWidget()
        self.show()
        # 主窗口布局实现略。。。

        # self.setWindowTitle('coggom')  # 设置标题
        # self.setWindowIcon(QIcon('icons.ico'))  # 设置标题图标
        # self.resize(240, 240)  # 设置窗体大小
        # self.setFixedSize(self.width(), self.height())  # 固定窗口大小
        # self.center()  # 窗体屏幕居中显示

        # self.layout = QVBoxLayout()

        # self.label = QLabel("Coggom the world ")

        # self.layout.addWidget(self.label)
        # self.setLayout(self.layout)
        self.tray()  # 程序实现托盘

    def tray(self):
        # 创建托盘程序
        ti = SystemTray(self)

    def center(self):
        # 窗口居中方法
        # 获得窗口
        qr = self.frameGeometry()
        # 获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        # 显示到屏幕中心
        qr.moveCenter(cp)
        self.move(qr.topLeft())


def kill_v2ray_process(name="v2ray"):
    child = subprocess.Popen(["pgrep", "-f", name],
                             stdout=subprocess.PIPE,
                             shell=False)
    if child.communicate()[0]:
        pid = int(
            subprocess.Popen(["pgrep", "-f", name],
                             stdout=subprocess.PIPE,
                             shell=False).communicate()[0])
        os.kill(pid, signal.SIGKILL)


if __name__ == "__main__":
    # 创建一个app程序
    os.chdir("/Applications/coggom.app/Contents/Resources")
    kill_v2ray_process()
    app = QApplication(sys.argv)
    # win = Window()
    w = Window()
    # QMainWindow.removeDockWidget(w)

    # w.close()
    # SystemTray(w)
    sys.exit(app.exec_())
