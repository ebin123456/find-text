from distutils.core import setup
import py2exe, sys, os
os.system("rm build -R")
os.system("rm dist -R")
sys.argv.append('py2exe')

setup(
    options = {'py2exe': {'bundle_files': 1, 'compressed': True}},
    console=['find.py'],
    zipfile = None,
)

os.rename('dist/find.exe','dist/find-text.exe')


# from distutils.core import setup
# import py2exe
  
# setup(console=['main.py'])