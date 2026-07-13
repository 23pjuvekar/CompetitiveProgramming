class Spreadsheet:

    def __init__(self, rows: int):
        self.cell_values = defaultdict(int)

    def setCell(self, cell: str, value: int) -> None:
        self.cell_values[cell] = value

    def resetCell(self, cell: str) -> None:
        if cell in self.cell_values:
            del self.cell_values[cell]

    def getValue(self, formula: str) -> int:
        if "+" in formula:
            cell1, cell2 = formula[1:].split("+")
            val1 = self.cell_values[cell1] if cell1[0].isalpha() else int(cell1)
            val2 = self.cell_values[cell2] if cell2[0].isalpha() else int(cell2)
            return val1 + val2
        else:
            cell = formula[1:]
            return self.cell_values[cell] if cell[0].isalpha() else int(cell)


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
