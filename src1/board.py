from properties import *
import tkinter as tk

class Board:
    def __init__(self) -> None:
        self.buttons = [[]]
        
    # mang luu tru cac nuoc di
    def set_board(self):
        return [[None] * columns for _ in range(rows)]
        

        