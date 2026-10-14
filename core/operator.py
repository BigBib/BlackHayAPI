from typing import Any, Tuple, List, Union
from .req import __modules__
from json import dumps
from .ram import RAM

def oper(cmd: Tuple[str, str]) -> Tuple[bool, str]:
    module, protocol = cmd
    if module == None or module.casefold() == "help" : print(dumps(__modules__, indent=2))
    else:
        for m in __modules__:
            if m["NameModule"] == module:
                answer = m["ModuleLink"](protocol)
                print("Data Recorded")
        return (True, answer[1])        
