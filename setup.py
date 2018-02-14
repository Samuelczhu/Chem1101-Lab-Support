import cx_Freeze
import sys
import os

os.environ['TCL_LIBRARY'] = "C:\\python\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\python\\tcl\\tk8.6"

base = None

if sys.platform == 'win32':
    base = "WIN32GUI"


executables = [cx_Freeze.Executable("Chem1101_Lab_Support.py",base=base,icon="icon.ico")]

cx_Freeze.setup(
    name = "Chem1101_Lab_Support",
    options = {"build_exe":{"packages":["tkinter"],"include_files":[os.path.join('C:\python','DLLs','tk86t.dll'),os.path.join('C:\python','DLLs','tcl86t.dll'),"icon.ico","image1.png","image2.png","image3.png","image4.png","image5.png","image6.png"]}},
    version = "0.1",
    description = "Chem1101 Lab application",
    executables = executables
    )
