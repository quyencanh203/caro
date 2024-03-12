import tkinter as tk
import math
import random

class CaroGame:
    def __init__(self, master, rows, columns):
        self.master = master
        self.rows = rows
        self.columns = columns
        self.count = 0
        self.current_player = 'X'
        self.create_board()

    def create_board(self):
        game_frame = tk.Frame(self.master, borderwidth=2, relief="ridge")
        game_frame.pack(padx=10, pady=10)

        self.buttons = [[None] * self.columns for _ in range(self.rows)]

        for i in range(self.rows):
            for j in range(self.columns):
                btn = tk.Button(game_frame, text="", width=5, height=2,
                                font=('Arial', 14),
                                command=lambda row=i, col=j: self.on_button_click(row, col))
                btn.grid(row=i, column=j, padx=3, pady=3)
                self.buttons[i][j] = btn

    def on_button_click(self, row, col):
        if not self.buttons[row][col]['text']:
            self.count += 1 
            print(f"player move {row} {col} count {self.count}")
            self.buttons[row][col]['text'] = self.current_player

            if self.check_winner(row, col):
                print(f"Player {self.current_player} wins!")
                self.disable_buttons()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                self.ai_move()

    # hàm kiểm tra chiến thắng 
    def check_winner(self, row, col):
        # Kiểm tra điều kiện chiến thắng theo bất kỳ hướng nào: ngang, dọc và chéo
        if self.check_line(row, col, 0, 1) or \
           self.check_line(row, col, 1, 0) or \
           self.check_line(row, col, 1, 1) or \
           self.check_line(row, col, 1, -1):
            return True
        return False
    
    # hàm kiểm tra ngang dọc 
    def check_line(self, row, col, delta_row, delta_col):
        # Lấy ký tự hiện tại của người chơi (X hoặc O)
        player = self.current_player
        # Khởi tạo biến đếm để theo dõi số lượng quân liên tiếp
        count = 0
    
        # Lặp qua một dãy vị trí xung quanh nước đi hiện tại
        for i in range(-4, 5):
            # Tính toán hàng và cột mới dựa trên các độ lệch
            new_row, new_col = row + i * delta_row, col + i * delta_col
    
            # Kiểm tra xem vị trí mới có nằm trong biên của bảng không
            if 0 <= new_row < self.rows and 0 <= new_col < self.columns:
                # Kiểm tra xem quân cờ tại vị trí mới thuộc về người chơi hiện tại hay không
                if self.buttons[new_row][new_col]['text'] == player:
                    # Tăng biến đếm cho các quân liên tiếp
                    count += 1
                    # Kiểm tra xem người chơi hiện tại có 5 quân liên tiếp không, đánh dấu chiến thắng
                    if count == 5:
                        return True
                else:
                    # Đặt lại biến đếm nếu dãy quân liên tiếp bị gián đoạn
                    count = 0
            else:
                # Đặt lại biến đếm nếu vị trí mới nằm ngoài biên
                count = 0
    
        return False
    

    def disable_buttons(self):
        for row in self.buttons:
            for btn in row:
                btn['state'] = 'disabled'

    def ai_move(self):
        # ai  alpha-beta pruning
        self.count += 1
        best_score, best_move = float('-inf'), None

        for i in range(self.rows):
            for j in range(self.columns):
                    
                if not self.buttons[i][j]['text']:
                    self.buttons[i][j]['text'] = 'O'
                    score = self.minimax(1, False, float('-inf'), float('inf'))
                    self.buttons[i][j]['text'] = ''

                    if score > best_score:
                        best_score = score
                        best_move = (i, j)

        if best_move:
            print(f"AI move {best_move[0]} {best_move[1]} count {self.count}")
            self.buttons[best_move[0]][best_move[1]]['text'] = 'O'
            if self.check_winner(best_move[0], best_move[1]):
                print("Player O wins!")
                self.disable_buttons()
            else:
                self.current_player = 'X'

    def minimax(self, depth, is_maximizing, alpha, beta):

        # Placeholder code
        if depth == 0 or random.random() < 0.1:
            # return random.randint(-10, 10)
            return self.evaluate_board()

        if is_maximizing:
            max_eval = float('-inf')
            for i in range(self.rows):
                for j in range(self.columns):
                    if not self.buttons[i][j]['text']:
                        self.buttons[i][j]['text'] = 'O'
                        eval_score = self.minimax(depth - 1, False, alpha, beta)
                        self.buttons[i][j]['text'] = ''
                        max_eval = max(max_eval, eval_score)
                        alpha = max(alpha, eval_score)
                        if beta <= alpha:
                            break
            return max_eval
        else:
            min_eval = float('inf')
            for i in range(self.rows):
                for j in range(self.columns):
                    if not self.buttons[i][j]['text']:
                        self.buttons[i][j]['text'] = 'X'
                        eval_score = self.minimax(depth - 1, True, alpha, beta)
                        self.buttons[i][j]['text'] = ''
                        min_eval = min(min_eval, eval_score)
                        beta = min(beta, eval_score)
                        if beta <= alpha:
                            break
            return min_eval
        
    def evaluate_board(self):
        player = self.current_player
        opponent = 'O' if player == 'X' else 'X'
    
        player_score = 0
        opponent_score = 0
    
        for i in range(self.rows):
            for j in range(self.columns):
                if self.buttons[i][j]['text'] == player:
                    player_score += self.evaluate_position(i, j, player)
                elif self.buttons[i][j]['text'] == opponent:
                    opponent_score += self.evaluate_position(i, j, opponent)
    
        return player_score - opponent_score
    
    def evaluate_position(self, row, col, player):
        score = 0
    
        # check ngang dọc chéo 
        for direction in [(0, 1), (1, 0), (1, 1), (1, -1)]:
            consecutive_count = self.count_consecutive(row, col, player, direction)
            score += self.score_consecutive(consecutive_count)
    
        return score
    
    def count_consecutive(self, row, col, player, direction):
        count = 0
        delta_row, delta_col = direction
    
        for i in range(-4, 5):
            new_row, new_col = row + i * delta_row, col + i * delta_col
    
            if 0 <= new_row < self.rows and 0 <= new_col < self.columns and self.buttons[new_row][new_col]['text'] == player:
                count += 1
            else:
                break
    
        return count
    
    def score_consecutive(self, count):
        # Gán điểm dựa trên số mảnh ghép liên tiếp
        if count == 5:
            return 10000
        elif count == 4:
            return 1000
        elif count == 3:
            return 100
        elif count == 2:
            return 10
        elif count == 1:
            return 1
        else:
            return 0
    
        
    
    
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Caro Game")
    root.geometry("1400x1100")

    game = CaroGame(root, rows=11, columns=11)

    root.mainloop()
