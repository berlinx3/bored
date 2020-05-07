from itertools import product
C = "ABCDEFGHI"
R = "123456789"

ALLCELLS = [c + r
           for c in C
           for r in R]
HORIZONTAL = [[c + r
               for c in C]
              for r in R]
VERTICAL = [[c + r
             for r in R]
            for c in C]

d1 = [c + r for c, r in zip(C,  R)]
d2 = [c + r for c, r in zip(C, reversed(R))]
DIAG = [d1, d2]
sqmap = [list(product(C[ci * 3: ci * 3 + 3],  R[ri * 3: ri * 3 + 3]))
         for ri in range(0, 3)
         for ci in range(0, 3)]
SQ = [list(map(lambda x: x[0] + x[1], sqmap[i]))
      for i in range(len(sqmap))]

FULLCOMBO = HORIZONTAL + VERTICAL + DIAG + SQ

NEIGHBOURS = {}
for cell in ALLCELLS:
    NEIGHBOURS[cell] = set()

for combo in FULLCOMBO:
    for v in combo:
        for n in combo:
            if v != n:
                NEIGHBOURS[v].add(n)


class SudokuBoard:
    def __init__(self, initBoard="." * 81):
        self.cells = {}
        for index, value in enumerate(initBoard):
            if value == ".":
                self.cells[ALLCELLS[index]] = R
            else:
                self.cells[ALLCELLS[index]] = value

    def __str__(self):
        s = ""
        for i in range(9):
            if i in [3, 6]:
                s += "---|---|---\n"
            for j in range(9):
                if j in [3, 6]:
                    s += "|"
                s += self.cells[HORIZONTAL[i][j]]
            s += "\n"
        return s


if __name__ == "__main__":
    board = SudokuBoard(
        "2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3")
