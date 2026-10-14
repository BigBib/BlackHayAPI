from .databay import __main__ as databay
from .ram import RAM
from typing import Tuple, Union, List

class Loadder:
    def DataBay(self, protocol: str) -> Tuple[bool, str]:
        try:
            if RAM("Servers").exists()[0] != True:
                status, msg = RAM("Servers").create()
                if status != True : raise Exception(msg)
                else:
                    if msg:
                        for server in msg:
                            if server != "" : RAM("Servers").write({"Server":server})
                        return (True, "ok")
        except Exception as e : return (False, e)

__modules__ = [
    {
        "NameModule":"databay",
        "Module":Loadder
    }
]
