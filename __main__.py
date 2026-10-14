from core import *
from concurrent.futures import ThreadPoolExecutor, as_completed
import core

if userData[0] != True : print("Ошибка -> %s" % (userData[1]))
else:
    answer, proxys = core.databay.__main__("socks5")
    if answer != True : print("Ошибка -> %s" % (proxys))
    else:
        if RAM("Servers").exists()[0] != True : RAM("Servers").create("list")
        if RAM("OpenedServers").exists()[0] != True : RAM("OpenedServers").create("list")
        with ThreadPoolExecutor(max_workers=len(RAM("Servers").getData()[1])) as thread:
            futu = {thread.submit(check, "socks5", server["server"]): server for server in RAM("Servers").getData()[1]}
            for f in as_completed(futu):
                answer, msg, country, server = f.result()
                print("%s - %s - %s [%s]" % (server, msg, answer, country))
                if asnwer == True : RAM("OpenedServers").write({"Server":server, "country":country})
        print(RAM("OpenedServers").getData()[1])
