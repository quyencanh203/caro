import tkinter as tk

from properties import *
from player import *
from ai import *
from board import *



class main:
    def __init__(self, master) -> None:
        self.current_player = player.player_move()
        self.master = master
        self.create_board()

 

    def create_board(self):
        # cai dat cho khung game
        game_frame = tk.Frame(self.master, border=2, relief= 'ridge')
        game_frame.pack(padx=10, pady=10)

        self.buttons = broad.set_board()

        # cai dat cho nut nhan trong game
        for i in range(rows):
            for j in range(columns):
                btn = tk.Button(game_frame, text="", width=5, height=2,
                                font=('Arial', 14),
                                command=lambda row=i, col=j: self.event_handling(row,col))
                # Đặt Button vào grid của Frame
                btn.grid(row=i, column=j, padx=3, pady=3)
                self.buttons[i][j] = btn  # Lưu trữ Button vào ma trận

    def event_handling(self, row, col):
        print(f"Clicked on row {row}, column {col}")

        if not self.buttons[row][col]['text']:

            self.buttons[row][col]['text'] = self.current_player

            if self.check_winner(row, col):
                print(f"Player {self.current_player} wins!")
                self.disable_buttons()
            else:
                if self.current_player == player.player_move():
                   self.current_player = ai.ai_move()
                else:
                   self.current_player = player.player_move()
 
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
            if 0 <= new_row < rows and 0 <= new_col < columns:
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
        # Tắt tất cả các Button khi có người chơi chiến thắng
        for row in self.buttons:
            for btn in row:
                btn['state'] = 'disabled'
        

if __name__ == "__main__":

    player = Player('X')
    ai = Ai('O')
    broad = Board()

    root = tk.Tk()
    root.title("Caro Game")
    root.geometry("1400x1100")

    game = main(root)

    root.mainloop()