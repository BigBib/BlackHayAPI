from typing import List, Tuple, Union
import requests

protocols: List = ["socks5", "socks4", "http", "https"]

def __main__(protocol: str = "socks5") -> Tuple[bool, Union[List[str], str]]:
    if protocol not in protocol : return (False, "Нет такого протокола в -> %s" % (protocols))
    try:
        req = requests.get("https://raw.githubusercontent.com/databay-labs/free-proxy-list/master/%s.txt" % (protocol))
        if req.status_code == 200 : return (True, req.txt.split("\n"))
        else : return (False, req.stauts_code)
    except BaseException as e : return (False, e)
