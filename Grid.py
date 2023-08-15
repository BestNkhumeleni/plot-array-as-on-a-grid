import tkinter as tk
import random

class GridApp:
    def __init__(self, root, rows, cols):
        self.root = root
        self.rows = rows
        self.cols = cols
        
        self.create_grid()
        #self.place_point()


    def create_grid(self):
        self.cells = [[None] * self.cols for _ in range(self.rows)]
        
        for i in range(self.rows):
            for j in range(self.cols):
                cell_frame = tk.Frame(self.root, width=50, height=50, highlightthickness=1, highlightbackground="black")
                cell_frame.grid(row=i, column=j)
                
                label = tk.Label(cell_frame, text="", width=6, height=2)
                label.pack(fill=tk.BOTH, expand=True)
                
                
                cell_frame.config(bg="blue")
                
                self.cells[i][j] = label
                
    def place_point(self, row , col):
        #row = random.randint(0, self.rows - 1)
        #col = random.randint(0, self.cols - 1)
        
        point_label = self.cells[row][col]
        point_label.config(text="((;))", font=("Helvetica", 14))
        

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Grid GUI with Point")
    
    num_rows = 10  # Adjust the number of rows
    num_cols = 10  # Adjust the number of columns
    
    app = GridApp(root, num_rows, num_cols)
    row = int(input("Which row do you wanna place a point : "))
    col = int(input("Which collumn do you wanna place a point: "))
    
    app.place_point(row, col)
    
    root.mainloop()
