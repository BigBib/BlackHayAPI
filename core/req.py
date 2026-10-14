from .databay import __main__ as databay
from .ram import RAM
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Tuple, Union, List, Optional
import requests, bs4, json

def loadUsers():
    

def load(protocol: str = "socks5") -> List[str]:
    
    l = databay()
    if l[0] != True : raise Exception("Ошибка %s" % (l[1]))
    if RAM("Servers").exists()[0] != True : RAM("Servers").create("list")
    else : RAM("Servers").delData()
    if RAM("OpenedServers").exists()[0] != True : RAM("OpenedServers").create("list")
    else : RAM("OpenedServers").delData()
    for server in l[1] : RAM("Servers").write(l[1])
    with ThreadPoolExecutor(max_workers=len(RAM("Servers").getData[1])) as thread:
        futu = {thread.submit(check(protocol, server["Server"])): server for server in RAM("Servers").getData()[1]}
        for f in as_completed(futu):
            asnwer, msg, country, server = f.result()
            print("%s - %s - %s [%s]" % (server, msg, answer, country))
            if answer == True : RAM("OpenedServers").write({"Server":server, "country":country})
    return json.dumps(RAM("OpenedServers").getData()[1])

def check(protocol: str, server: str = None) -> Tuple[bool, str, Optional[str], Optional[str]]:
    if server == None : return (False, "Сервер не указан", None, None)
    proxy_body = {
        "http":"http://%s" % (server) if protocol.casefold() == "http" or protocol.casefold() == "https" else ("socks4://%s" % (server) if protocol.casefold() == "socks4" else ("socks5://%s" % (server) if protocol.casefold() == "socks5" else None)),
        "https":"https://%s" % (server) if protocol.casefold() == "http" or protocol.casefold() == "https" else ("socks4://%s" % (server) if protocol.casefold() == "socks4" else ("socsk5://%s" % (server) if protocol.casefold() == "socks5" else None))
    }
    if proxy_body["http"] == None and proxy_body["https"] == None : return (False, "Протокол указан неверно", None, None)
    if RAM("User").exists()[0] != True : return (False, "Данные по пользователю не указаны", None, None)
    else:
        try:
            req = requests.get("http://ip-api.com/json" if protocol == "http" else "https://api.ipify.org/?format=json", proxies=proxy_body)
            if req.status_code == 200
                body = bs4.BeautifulSoup(req.text, "html.parser").text
                if body:
                    if json.loads(body)["query" if protocol == "http" else "ip"] != RAM("User").getData()[1]["IP"] : return (True, "Сервер работает", json.loads(body)["country"] if protocol == "http" else None, server)
                    else : return (False, "Сервер не работает", None, server)
            else : return (False, "!=200", None, server)
        except requests.exceptions.ConnectionError : return (False, "Не удалось подключиться к сервер", None, server)
        except requests.exceptions.ConnectTimeout : return (False, "Время ожидания истекло", None, server)
        except requests.exceptions.ReadTimeout : return (False, "Время ожидания истекло", None, server)
        except requests.exceptions.ChunkedEncodingError : return (False, "Разрыв", None, server)
