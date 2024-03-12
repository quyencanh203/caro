class CaroGame:
    def __init__(self, rows, columns) -> None:
        self.rows = rows
        self.columns = columns
        self.current_player = 'X'
        self.create_table()
        self.buttons =[[]]


    def create_table(self):
        # mang luu cac nuoc di
        self.buttons = [[None]*self.columns for _ in range(self.rows)]
        
        pass
        
if __name__ == "__main__":
     print('nhap kich thuoc game n :')
     n = int(input())
     print('nhap so nuoc da di m :')
     m = int(input())
     print('nhap toa do (x,y) cua cac nuoc da di')
    
     game_on = CaroGame(n,n)
