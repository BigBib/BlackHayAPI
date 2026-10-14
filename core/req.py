from .databay import __main__ as databay
from .ram import RAM
from typing import Tuple, Union, List, Optional
import requests, bs4, json

class Loadder:
    def DataBay(self, protocol: str) -> Tuple[bool, str]:
        try:
            if RAM("Servers").exists()[0] != True:
                status, msg = RAM("Servers").create()
                if status != True : raise Exception(msg)
                if msg:
                    for server in msg:
                        if server != "" : RAM("Servers").write({"Server":server})
                    return (True, "ok")
        except Exception as e : return (False, e)

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

__modules__ = [
    {
        "NameModule":"databay",
        "ModuleLing":Loadder().Databay
    }
]
