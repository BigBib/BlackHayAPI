from typing import Union, Tuple, List, Any, Dict

class RAM:

    typeCells: List[str] = ["json", "list"]

    cells: List[Dict] = []
    nameIndex: Dict[str, int] = {}

    def __init__(self, NameCell: str) : self.name = NameCell

    def exists(self) -> bool:
        if self.name in self.nameIndex : return True
        else : return False

    def create(self, TypeCell: str) -> Tuple[bool, str]:
        try:
            if self.exists() != False : return (False, "Ячейка уже существует")
            else:
                if TypeCell.casefold() not in self.typeCells : return (False, "Такого формата не существует")
                else:
                    if self.cells.append({"Data":{} if TypeCell.casefold() == "json" else [], "TypeCell":TypeCell}) : self.nameIndex.update({self.name:len(self.cells)-1})
                    return (True, "Ячейка создана")
        except BaseException as e : return (False, e)

    def write(self, data: Dict[Any, Any]) -> Tuple[bool, str]:
        try:
            if self.exists() != True : return (False, "Ячейки не существует")
            else : self.cells[self.nameIndex[self.name]]["Data"].update(data) if self.cells[self.nameIndex[self.name]]["TypeCell"].casefold() == "json" else self.cells[self.nameIndex[self.name]]["Data"].append(data)
            return (True, "Запись произведена")
        except BaseException as e : return (False, e)

    def getData(self) -> Tuple[bool, Union[List[Dict], Dict, str]]:
        try:
            if self.exists() != True : return (False, "Ячейки не существует")
            else : return (True, self.cells[self.nameIndex[self.name]]["Data"])
        except BaseException as e : return (False, e)

    def getCellsName(self) -> Tuple[bool, Union[List[str], str]]:
        try:
            cells = []
            for cell in self.nameIndex : cells.append(cell)
            return (True, cells)
        except BaseException as e : return (False, e)

    def delData(self) -> Tuple[bool, str]:
        try:
            if self.exists() != True : return (False, "Ячейки не существует")
            else : self.cells[self.nameIndex[self.name]]["Data"].clear()
            return (True, "Данные удалены")
        except BaseException as e : return (False, e)
    
    def delCell(self) -> Tuple[bool, str]:
        try:
            if self.exists() != True : return (False, "Ячейки не существует")
            else:
                del self.cells[self.nameIndex[self.name]], self.nameIndex[self.name]
                return (True, "Ячейка удалена")
        except BaseException as e : return (False, e)
