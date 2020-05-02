from enum import Enum
from util import Board, Piece, find_best_move, find_best_move_alphabeta

class C4Piece(Piece, Enum):
    B = "B"
    R = "R"
    E = " "

    @property
    def opposite(self):
        if self == C4Piece.B:
            return C4Piece.R
        elif self == C4Piece.R:
            return C4Piece.B
        else:
            return C4Piece.E
    
    def __str__(self):
        return self.value

    
def generate_segments(num_columns, num_rows, segment_length):
    segments = []

    for c in range(num_columns):
        for r in range(num_rows - segment_length + 1):
            segment = []
            for t in range(segment_length):
                segment.append((c, r + t))
            segments.append(segment)

    for c in range(num_columns - segment_length + 1):
        for r in range(num_rows):
            segment = []
            for t in range(segment_length):
                segment.append((c + t, r))
            segments.append(segment)

    for c in range(num_columns - segment_length  + 1):
        for r in range(num_rows - segment_length + 1):
            segment = []
            for t in range(segment_length):
                segment.append((c + t, r + t))
            segments.append(segment)

    for c in range(num_columns - segment_length + 1):
        for r in range(segment_length - 1, num_rows):
            segment = []
            for t in range(segment_length):
                segment.append((c + t, r - t))
            segments.append(segment)

    return segments

    

class C4Board(Board):
    NUM_ROWS = 6
    NUM_COLUMNS = 7
    SEGMENT_LENGTH = 4
    SEGMENTS = generate_segments(NUM_COLUMNS, NUM_ROWS, SEGMENT_LENGTH)

    class Column:
        def __init__(self):
            self._container = []

        @property
        def full(self):
            return len(self._container) == C4Board.NUM_ROWS

        def push(self, item):
            if self.full:
                raise OverflowError("Trying to push piece to full column")
            
            self._container.append(item)

        def __getitem__(self, index):
            if index > len(self._container) - 1:
                return C4Piece.E
            return self._container[index]

        def __repr__(self):
            return repr(self._container)

        def copy(self):
            temp = C4Board.Column()
            temp._container = self._container.copy()
            return temp

    def __init__(self, position = None, turn = C4Piece.B):

        if position is None:
            self.position = [C4Board.Column() for _ in range(C4Board.NUM_COLUMNS)]
        else:
            self.position = position
        
        self._turn = turn

    @property
    def turn(self):
        return self._turn
        
    def move(self, location):
        temp_position = self.position.copy()
        for c in range(C4Board.NUM_COLUMNS):
            temp_position[c] = self.position[c].copy()
        
        temp_position[location].push(self._turn)
        return C4Board(temp_position, self._turn.opposite)

    @property
    def legal_moves(self):
        return [c for c in range(C4Board.NUM_COLUMNS)
                    if not self.position[c].full]

    def _count_segment(self, segment):
        black_count = 0
        red_count = 0
        for column, row in segment:
            if self.position[column][row] == C4Piece.B:
                black_count += 1
            elif self.position[column][row] == C4Piece.R:
                red_count += 1

        return black_count, red_count

    @property
    def is_win(self):
        for segment in C4Board.SEGMENTS:
            black_count, red_count = self._count_segment(segment)
            
            if black_count == 4 or red_count == 4:
                return True
        return False

    def _evaluate_segment(self, segment, player):
        black_count, red_count = self._count_segment(segment)

        if red_count > 0 and black_count > 0:
            return 0
        
        count = max(red_count, black_count)
        score = 0

        if count == 2:
            score = 1
        elif count == 3:
            score = 100
        elif count == 4:
            score = 1000000

        color = C4Piece.B
        if red_count > black_count:
            color = C4Piece.R
        
        if color != player:
            return -score
        return score

    def evaluate(self, player):
        total = 0
        for segment in C4Board.SEGMENTS:
            total += self._evaluate_segment(segment, player)
        return total

    def __repr__(self):
        display = ""
        for r in reversed(range(C4Board.NUM_ROWS)):
            display += "|"

            for c in range(C4Board.NUM_COLUMNS):
                display += f"{self.position[c][r]}" + "|"
            display += "\n"

        return display

def get_player_move():
    player_move = -1
    while player_move not in board.legal_moves:
        play = int(input('Enter a legal column (0-6):'))
        player_move = play
    return player_move



if __name__ == "__main__":

    board = C4Board()

    while True:
        human_move = get_player_move()
        board = board.move(human_move)
        if board.is_win:
            print("Human wins!")
            break
        elif board.is_draw:
            print("Draw!")
            break

        computer_move = find_best_move_alphabeta(board, 3)
        print(f"Computer move is {computer_move}")
        board = board.move(computer_move)
        print(board)

        if board.is_win:
            print("Computer wins!")
            break
        elif board.is_draw:
            print("Draw!")
            break
