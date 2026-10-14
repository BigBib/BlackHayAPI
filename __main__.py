from core import *
import sys, os

d = r"""
 .+"+.+"+.+"+.+"+.+"+.+"+. 
(      ____  _   _        )
 )    | __ )| | | |      ( 
(     |  _ \| |_| |       )
 )    | |_) |  _  |      ( 
(     |____/|_| |_|       )
 )                       ( 
(                         )
 "+.+"+.+"+.+"+.+"+.+"+.+"
"""

def main()
    os.system("cls") if os.sys.platform == "win32" else os.system("clear")
    print(d)
    work: bool = True
    ignore_protocol: bool = True if "http" in sys.argv or "https" in sys.argv or "socks4" in sys.argv or "socks5" in sys.argv else False
    while work:
        cmd = input("> ")
        if cmd == "exit" : work = False
        elif cmd == "getServers" : print(RAM("OpenedServers").getData()[1])
        elif cmd == "clear" : os.system("cls") if os.sys.platform == "win32" else os.system("clear")
        elif cmd == "__loadRAM" : print(RAM.cells), print("\n%s" % (RAM.nameIndex))
        else:
            if ignore_protocol == True:
                call = oper((cmd, sys.argv[2]))
                print(call[1]) if sys.argv[1] == "--debug" else print()
            else:
                protocol = input("databay[protocol]> ")
                call = oper((cmd, protocol))
                print(call[1]) if sys.argv[1] == "--debug" else print()

if __name__ == "__main__" : main()
