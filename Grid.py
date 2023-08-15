import tkinter as tk
import random

class GridApp:
    def __init__(self, root, rows, cols):
        self.root = root
        self.rows = rows
        self.cols = cols
        
        self.create_grid()
        self.place_point()

    def create_grid(self):
        self.cells = [[None] * self.cols for _ in range(self.rows)]
        
        for i in range(self.rows):
            for j in range(self.cols):
                label = tk.Label(self.root, text="", width=6, height=2, relief=tk.RIDGE)
                label.grid(row=i, column=j)
                self.cells[i][j] = label
                
    def place_point(self):
        row = random.randint(0, self.rows - 1)
        col = random.randint(0, self.cols - 1)
        
        point_label = self.cells[row][col]
        point_label.config(text="*", font=("Helvetica", 14))

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Grid GUI with Point")
    
    num_rows = 3
    num_cols = 3
    
    app = GridApp(root, num_rows, num_cols)
    
    root.mainloop()