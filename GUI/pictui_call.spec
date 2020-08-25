# -*- mode: python -*-

block_cipher = None


a = Analysis(['pictui_call.py'],
             pathex=['C:\\work\\VSANA\\src\\life_game\\GUI_HumanLike'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[
             'matplotlib', 
             'pandas', 
             'PyQt4', 
             'Jinja2', 
             'Keras', 
             'Flask', 
             'mysql-connector-python', 
             'PyInstaller',
             'Pillow',
             'PyAudio',
             'PyQt5Designer',
             'twitter',
             'SQLAlchemy',
             'Sphinx',
             'PyOpenGL',
             'Markdown',
             'MarkupSafe',
             'beautifulsoup4',
             'Pygments',
             'PuLP',
             'PythonQwt'
             ],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
a.datas += [('resources/maru25.png', '.\\resources/maru25.png', 'DATA')]
a.datas += [('resources/batsu25.png', '.\\resources/batsu25.png', 'DATA')]
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='pictui_call',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
