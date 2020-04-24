import webbrowser
from ctypes import *

x = 0x3F
a = windll.kernel32

def func():
    webbrowser.open('https://www.youtube.com')

if __name__=='__main__':
    func()
        