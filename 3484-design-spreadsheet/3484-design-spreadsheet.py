class Spreadsheet:

    def __init__(self, rows: int):
        self.cells = {}

    def setCell(self, cell: str, value: int) -> None:
        self.cells[cell] = value
        
    def resetCell(self, cell: str) -> None:
        if cell in self.cells:
            del self.cells[cell]

    def getCellValue(self, cell_or_int):
        x = 0
        try:
            x = int(cell_or_int)
        except:
            x = self.cells.get(cell_or_int, 0)
        return x

    def getValue(self, formula: str) -> int:
        formula = formula[1:]
        a,b = formula.split("+")
        return self.getCellValue(a) + self.getCellValue(b)
        
