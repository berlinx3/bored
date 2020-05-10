from util import SudokuBoard, FULLCOMBO, NEIGHBOURS
from functools import reduce
from heapq import heappop, heappush


class Cell_Container:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    @property
    def possibility_length(self):
        return len(self.value)

    def __lt__(self, other):
        return self.possibility_length < other.possibility_length


class Solver:

    @classmethod
    def naked_twins(cls, cells):
        visited = set()
        twins = set()

        while True:
            duos = [key for key, value in cells.items()
                    if len(value) == 2]

            twins.clear()

            for d1 in duos:
                for d2 in duos:
                    if d1 != d2:
                        if cells[d1] == cells[d2]:
                            if d2 in NEIGHBOURS[d1]:
                                if (d1, d2) not in twins and (d2, d1) not in twins:
                                    twins.add((d1, d2))

            if len(visited) == len(twins):
                break

            for twin in twins:
                visited.add(twin)
                neighbours = NEIGHBOURS[twin[0]].intersection(
                    NEIGHBOURS[twin[1]])

                two_values = cells[twin[0]]
                for neighbour in neighbours:
                    for two_value in two_values:
                        cells[neighbour] = cells[neighbour].replace(
                            two_value, "")

    @classmethod
    def only_choice(cls, cells):
        visited = set()
        while True:
            only_ones = [key for key, value in cells.items()
                         if len(value) == 1]

            if len(only_ones) == 81 or len(only_ones) <= len(visited):
                break

            for only_one in only_ones:
                if only_one not in visited:
                    one_value = cells[only_one]
                    visited.add(only_one)
                    for neighbour in NEIGHBOURS[only_one]:
                        cells[neighbour] = cells[neighbour].replace(
                            one_value, "")

    @classmethod
    def eliminate(cls, cells):
        old_count = 0

        while True:
            new_count = sum(list(map(len, cells.values())))

            if new_count == 81 or new_count == old_count:
                break

            cls.only_choice(cells)
            cls.naked_twins(cells)
            old_count = new_count

    @classmethod
    def is_consistent(cls, cells):
        all_values = set()

        for combo in FULLCOMBO:
            all_values.clear()
            for cell in combo:
                all_values.add(cells[cell])

            if len(all_values) != 9:
                return False

        return True

    @classmethod
    def search(cls, cells):
        cls.eliminate(cells)

        candidates = []

        for key, value in cells.items():
            if len(value) == 0:
                return None
            elif len(value) != 1:
                heappush(candidates, Cell_Container(key, value))

        if not candidates:
            if cls.is_consistent(cells):
                return cells
            else:
                return None

        candidate = heappop(candidates)
        del candidates

        for value in cells[candidate.key]:
            cells_copy = cells.copy()
            cells_copy[candidate.key] = value

            result = cls.search(cells_copy)

            if result is not None:
                return result

        return None

    @classmethod
    def solve(cls, board):
        result = cls.search(board.cells)
        if result is not None:
            board.cells = result
            return board
        
        return None


if __name__ == "__main__":
    board = SudokuBoard(
        "2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3")
    board = Solver.solve(board)

    if board is not None:
        print(board)
    else:
        print("No solution found!")
