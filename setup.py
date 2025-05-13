
from setuptools import setup

APP = ['clipboard_manager.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': False,    
    'iconfile': 'icon.icns',

    'plist': {
        'LSUIElement': True,  
        'CFBundleName': 'ClipboardManager',
        'CFBundleDisplayName': 'Clipboard Manager',
        'CFBundleIdentifier': 'com.yourdomain.clipboardmanager',
        'CFBundleVersion': '1.0.0',
        'CFBundleShortVersionString': '1.0.0',
    },
    'packages': ['rumps', 'pyperclip'], 
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)

