#!d:\stuff\pycharmprojects\toyota_store\venv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pycycle==0.0.8','console_scripts','pycycle'
__requires__ = 'pycycle==0.0.8'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pycycle==0.0.8', 'console_scripts', 'pycycle')()
    )
