from enum import Enum
from util import Piece, Board, find_best_move
import unittest

class TTTPiece(Piece, Enum):
    X = "X"
    O = "O"
    E = " "

    @property
    def opposite(self):
        if self == TTTPiece.X:
            return TTTPiece.O
        elif self == TTTPiece.O:
            return TTTPiece.X
        else:
            return TTTPiece.E
    
    def __str__(self):
        return self.value


class TTTBoard(Board):
    def __init__(self, position = [TTTPiece.E] * 9, turn = TTTPiece.X):
        self.position = position
        self._turn = turn

    @property
    def turn(self):
        return self._turn

    def move(self, location):
        temp_position = self.position.copy()
        temp_position[location] = self._turn
        return TTTBoard(temp_position, self._turn.opposite)

    @property
    def legal_moves(self):
        return [l for l in range(len(self.position))
                    if self.position[l] == TTTPiece.E ]

    
    @property
    def is_win(self):
        return self.position[0] == self.position[1] and self.position[0] == self.position[2] and self.position[0] != TTTPiece.E or \
               self.position[3] == self.position[4] and self.position[3] == self.position[5] and self.position[3] != TTTPiece.E or \
               self.position[6] == self.position[7] and self.position[6] == self.position[8] and self.position[6] != TTTPiece.E or \
               self.position[0] == self.position[3] and self.position[0] == self.position[6] and self.position[0] != TTTPiece.E or \
               self.position[1] == self.position[4] and self.position[1] == self.position[7] and self.position[1] != TTTPiece.E or \
               self.position[2] == self.position[5] and self.position[2] == self.position[8] and self.position[2] != TTTPiece.E or \
               self.position[0] == self.position[4] and self.position[0] == self.position[8] and self.position[0] != TTTPiece.E or \
               self.position[2] == self.position[4] and self.position[2] == self.position[6] and self.position[2] != TTTPiece.E
               
    def evaluate(self, player):
        if self.is_win and self.turn == player:
            return -1
        elif self.is_win and self.turn !=player:
            return 1
        else:
            return 0
        
    def __repr__(self):
        return f"""{self.position[0]}|{self.position[1]}|{self.position[2]}
---
{self.position[3]}|{self.position[4]}|{self.position[5]}
---
{self.position[6]}|{self.position[7]}|{self.position[8]}"""



class TTTMinimaxTestCase(unittest.TestCase):
    def test_easy_position(self):
        to_win_easy_position = [ TTTPiece.X, TTTPiece.O, TTTPiece.X,
                                 TTTPiece.X, TTTPiece.E, TTTPiece.O,
                                 TTTPiece.E, TTTPiece.E, TTTPiece.O]

        test_board = TTTBoard(to_win_easy_position, TTTPiece.X)
        answer = find_best_move(test_board)
        self.assertEqual(answer, 6)

    
    def test_block_position(self):
        
        to_block_position = [ TTTPiece.X, TTTPiece.E, TTTPiece.E,
                              TTTPiece.E, TTTPiece.E, TTTPiece.O,
                              TTTPiece.E, TTTPiece.X, TTTPiece.O]

        test_board = TTTBoard(to_block_position, TTTPiece.X)
        answer = find_best_move(test_board)
        self.assertEqual(answer, 2)

        
    
    def test_hard_position(self):
        
        to_win_hard_position = [ TTTPiece.X, TTTPiece.E, TTTPiece.E,
                                 TTTPiece.E, TTTPiece.E, TTTPiece.O,
                                 TTTPiece.O, TTTPiece.X, TTTPiece.E]

        test_board = TTTBoard(to_win_hard_position, TTTPiece.X)
        answer = find_best_move(test_board)
        self.assertEqual(answer, 1)



def get_player_move():
    player_move = -1
    while player_move not in board.legal_moves:
        play = int(input('Enter a legal square (0-8):'))
        player_move = play
    return player_move



if __name__ == "__main__":
    # unittest.main()

    board = TTTBoard()

    while True:
        human_move = get_player_move()
        board = board.move(human_move)

        if board.is_win:
            print("Human wins")
            break
        elif board.is_draw:
            print("Draw!")
            break

        computer_move = find_best_move(board)
        print(f"Computer move is {computer_move}")

        board = board.move(computer_move)
        print(board)

        if board.is_win:
            print("Computer wins!")
            break
        elif board.is_draw:
            print("Draw!")
            break