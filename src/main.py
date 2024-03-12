import tkinter as tk

class CaroGame:
    # hàm khời tạo constructor 
    def __init__(self, master, rows, columns):
        # Khởi tạo đối tượng CaroGameGUI với cửa sổ chính, số hàng và số cột
        self.master = master  # biến tham chiếu đến cửa sổ chính của ứng dụng 
        self.rows = rows
        self.columns = columns
        self.current_player = 'X'  # Người chơi hiện tại, bắt đầu là 'X'
        self.create_board()

    # hàm tạo bảng game 
    def create_board(self):
        # Tạo bảng game với các ô là các Button trong giao diện Tkinter
        game_frame = tk.Frame(self.master, borderwidth=2, relief="ridge")
        game_frame.pack(padx=10, pady=10)

        # Ma trận lưu trữ các Button trong bảng
        self.buttons = [[None] * self.columns for _ in range(self.rows)]

        for i in range(self.rows):
            for j in range(self.columns):
                # Tạo Button với các thuộc tính cơ bản
                btn = tk.Button(game_frame, text="", width=5, height=2,
                                font=('Arial', 14),
                                command=lambda row=i, col=j: self.on_button_click(row, col))

                # Đặt Button vào grid của Frame
                btn.grid(row=i, column=j, padx=3, pady=3)
                self.buttons[i][j] = btn  # Lưu trữ Button vào ma trận

    # hàm xử lý sự kiện 
    def on_button_click(self, row, col):
        # Xử lý sự kiện khi một Button được click
        print(f"Clicked on row {row}, column {col}")

        # Kiểm tra xem ô đã được đánh chưa
        if not self.buttons[row][col]['text']:
            # Đặt ký tự của người chơi vào ô
            self.buttons[row][col]['text'] = self.current_player

            # Kiểm tra xem người chơi hiện tại đã chiến thắng chưa
            if self.check_winner(row, col):
                print(f"Player {self.current_player} wins!")
                self.disable_buttons()  # Tắt tất cả Button khi có người chơi chiến thắng
            else:
                # Chuyển lượt cho người chơi tiếp theo
                self.current_player = 'O' if self.current_player == 'X' else 'X'
    
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
        # Tắt tất cả các Button khi có người chơi chiến thắng
        for row in self.buttons:
            for btn in row:
                btn['state'] = 'disabled'


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Caro Game")
    root.geometry("1400x1100")

    game = CaroGame(root, rows=12, columns=19)

    root.mainloop()
