# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['/Users/quan/Developer/Python/QTv2client'],
             binaries=[],
             datas=[("/Users/quan/Developer/Python/QTv2client/icon.ico",
             "."),("/Users/quan/Developer/Python/QTv2client/config.json",
             "."),("/Users/quan/Developer/Python/QTv2client/v2ray/*","./v2ray")],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='main')
app = BUNDLE(coll,
             name='coggom.app',
             version="0.0.1",
             icon="/Users/quan/Downloads/paper-plane_40433.icns",
             bundle_identifier=None)
