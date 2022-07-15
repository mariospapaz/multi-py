# -*- mode: python ; coding: utf-8 -*-


import platform

_WINDOWS = "Windows"
_LINUX = "Linux"
_MAC = "Darwin"

host_os = platform.system()

if host_os not in (_WINDOWS, _LINUX, _MAC):
    txt = f"""
    Unrecognized operating system: {host_os}
    """
    raise ValueError(txt)

if host_os == _MAC:
    _MAC = "MacOS"

architecture = platform.machine()


block_cipher = None

import os 

files = os.listdir('.')

exceptions = "main.py", "ignore-me.sh", "requirements.txt", "executables"


stuff = []
for file in files:
    if file not in exceptions:
        if os.path.isdir(file):
            stuff.append(tuple([file, file]))
        elif os.path.isfile(file):
            stuff.append(tuple([file, '.']))

print(f"""
#################################################

OPERATING SYSTEM: {host_os}

CPU ARCHITECTURE: {architecture}

FILES: {files}

DATA FOUND: {stuff}

#################################################
""")


a = Analysis(
    ['../main.py'],
    pathex=[],
    binaries=[],
    datas=stuff,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name=f'main {host_os} {architecture}',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
