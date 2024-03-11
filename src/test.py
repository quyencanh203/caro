import tkinter as tk

class CaroGameGUI:
    def __init__(self, master, rows, columns):
        self.master = master
        self.rows = rows
        self.columns = columns
        self.current_player = 'X'  # Bắt đầu với người chơi X
        self.create_board()
    
    def create_board(self):
        # Tạo một Frame để chứa khung trò chơi
        game_frame = tk.Frame(self.master, borderwidth=2, relief="ridge")
        game_frame.pack(padx=10, pady=10)

        # Tạo ma trận chứa các ô cờ, ban đầu mỗi ô là None
        self.buttons = [[None] * self.columns for _ in range(self.rows)]

        for i in range(self.rows):
            for j in range(self.columns):
                # Tạo nút (ô cờ) với các thuộc tính cụ thể
                btn = tk.Button(game_frame, text="", width=8, height=3,
                                font=('Arial', 14),
                                command=lambda row=i, col=j: self.on_button_click(row, col))
                
                # Đặt nút vào cửa sổ theo tọa độ hàng và cột trong Frame
                btn.grid(row=i, column=j, padx=5, pady=5)
                
                # Lưu trữ nút vào ma trận để tham chiếu sau này
                self.buttons[i][j] = btn

    def on_button_click(self, row, col):
        # Xử lý sự kiện khi người chơi nhấn vào ô cờ tại hàng `row` và cột `col`
        print(f"Clicked on row {row}, column {col}")
        # Kiểm tra xem ô cờ đã được chọn có trống không
        if not self.buttons[row][col]['text']:
            # Cập nhật nút với ký tự của người chơi hiện tại (X hoặc O)
            self.buttons[row][col]['text'] = self.current_player
            # Kiểm tra xem có người chiến thắng sau mỗi lần di chuyển không
            if self.check_winner(row, col):
                print(f"Player {self.current_player} wins!")
                self.disable_buttons()  # Tắt tất cả nút khi có người chiến thắng
            else:
                # Chuyển đến người chơi kế tiếp
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self, row, col):
        # Thực hiện logic kiểm tra người chiến thắng
        # Bạn cần kiểm tra theo chiều ngang, dọc và chéo
        # Bạn có thể thêm mã kiểm tra dòng và cột, và chéo tại đây
        
        # check ngang
        if self.buttons[row][col]['text'] == self.buttons[row][col-1]['text']:
            if self.buttons[row][col]['text'] == self.buttons[row][col-1]['text']:
               return True
        
                


    def disable_buttons(self):
        # Tắt tất cả nút sau khi trò chơi kết thúc
        for row in self.buttons:
            for btn in row:
                btn['state'] = 'disabled'

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Caro Game")
    root.geometry("580x400")

    game = CaroGameGUI(root, rows=4, columns=5)

    root.mainloop()