class Spreadsheet:

    def __init__(self, rows: int):
        self.cells = defaultdict(list)
        

    def setCell(self, cell: str, value: int) -> None:
        self.cells[cell] = value

    def resetCell(self, cell: str) -> None:
        self.cells[cell] = 0

    def getValue(self, formula: str) -> int:
        
        for i in range(1,len(formula)):

            if formula[i] == '+':
                s1,s2 = formula[1:i], formula[i+1:]
                left = self.cells.get(s1,0) if s1[0].isalpha() else int(s1)
                right = self.cells.get(s2,0) if s2[0].isalpha() else int(s2)
                return left + right
        

        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)