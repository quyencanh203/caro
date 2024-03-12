

from entity import *
from properties import *

class Ai(Entity):
    def __init__(self, text) -> None:
        super().__init__(text)

    @staticmethod
    def ai_move(board):
        best_move = Ai.minimax_ab(board, True, 3, float('-inf'), float('inf'))
        return best_move

    @staticmethod
    def minimax_ab(board, is_maximizing_player, depth, alpha, beta):
        if depth == 0 or board.is_game_over():
            return Ai.evaluate_board(board)

        if is_maximizing_player:
            max_eval = float('-inf')
            for move in board.get_available_moves():
                board.make_move(move, 'O')
                eval = Ai.minimax_ab(board, False, depth - 1, alpha, beta)
                board.undo_move(move)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            for move in board.get_available_moves():
                board.make_move(move, 'X')
                eval = Ai.minimax_ab(board, True, depth - 1, alpha, beta)
                board.undo_move(move)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    @staticmethod
    def evaluate_board(board):
        # Đánh giá số lượng dòng, cột, đường chéo có thể thắng cho AI và người chơi
        ai_score = 0
        player_score = 0

        for row in range(rows):
            for col in range(columns):
                if board[row][col] == 'O':
                    ai_score += Ai.calculate_score(board, row, col)
                elif board[row][col] == 'X':
                    player_score += Ai.calculate_score(board, row, col)

        return ai_score - player_score

    @staticmethod
    def calculate_score(board, row, col):
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        score = 0

        for direction in directions:
            score += Ai.calculate_line_score(board, row, col, *direction)

        return score

    @staticmethod
    def calculate_line_score(board, row, col, delta_row, delta_col):
        ai_count = 0
        player_count = 0

        for i in range(-4, 5):
            new_row, new_col = row + i * delta_row, col + i * delta_col

            if 0 <= new_row < rows and 0 <= new_col < columns:
                if board[new_row][new_col] == 'O':
                    ai_count += 1
                elif board[new_row][new_col] == 'X':
                    player_count += 1

        # Xác định điểm số cho dòng hiện tại
        if ai_count == 4:
            return 100  # AI có 4 quân liên tiếp, gần chiến thắng
        elif ai_count == 3 and player_count == 0:
            return 10  # AI có 3 quân liên tiếp, có thể tạo thành 4
        elif ai_count == 2 and player_count == 0:
            return 1   # AI có 2 quân liên tiếp, có thể tạo thành 3
        elif player_count == 4:
            return -100  # Người chơi có 4 quân liên tiếp, gần chiến thắng
        elif player_count == 3 and ai_count == 0:
            return -10  # Người chơi có 3 quân liên tiếp, có thể tạo thành 4
        elif player_count == 2 and ai_count == 0:
            return -1   # Người chơi có 2 quân liên tiếp, có thể tạo thành 3

        return 0  # Không có quân liên tiếp trong dòng này