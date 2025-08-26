# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['csnova.py'],
    pathex=[],
    binaries=[],
    datas=[('core/translations', 'core/translations'), ('core/tables', 'core/tables'), ('data', 'data'), ('assets', 'assets'), ('config', 'config'), ('gui/styles', 'gui/styles'), ('docs', 'docs'), ('ai', 'ai'), ('export', 'export')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='csnova',
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
