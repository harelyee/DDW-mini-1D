#!C:\Users\harel\Desktop\d2w_mini_projects\mp_calc\virtenv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'Transcrypt==3.7.16','console_scripts','transcrypt'
__requires__ = 'Transcrypt==3.7.16'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('Transcrypt==3.7.16', 'console_scripts', 'transcrypt')()
    )
