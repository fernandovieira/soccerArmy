#!C:/Users/Fernando/Miniconda3/envs/soccerArmy\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'Twisted==16.4.1','console_scripts','twistd'
__requires__ = 'Twisted==16.4.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('Twisted==16.4.1', 'console_scripts', 'twistd')()
    )
