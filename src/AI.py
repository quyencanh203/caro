# AI.py
import math

class AIPlayer:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.opponent = 'O'
        self.player = 'X'

    def make_move(self, board):
        pass
    
    # hàm tính giá trị minimaxab của nước đi 
    def minimaxab(self, board, depth, alpha, beta, maximizing_player):
        pass

    # hàm dự đoán nước đi tốt nhất 
    def evaluate_board(self, board):
        # You can implement your own heuristic evaluation function here
        return 0
    

