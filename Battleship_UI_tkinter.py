#I'm unsure which to use, I'll just try both until one hits a roadblock

'''
NOTICE:

DUE TO VSCODE ISSUES, I NOW HAVE TO WRITE THE CODE IN HERE AND THEN RUN/TEST THROUGH THE PYTHON IDLE, INSTEAD OF VSCODE'S RUNNER. PLEASE FORGIVE ANY SLIGHT ODDITIES IN TIMING CAUSED BY THIS.

For some reason vscode is randomly adding "" arround my file names, causing it to look for a file that doesn't exist instead of the actual file I need to run.
'''


import tkinter as tk
from math import floor

Targeting_Grid = tk.Tk()

Targeting_Grid.geometry("500x500")
Targeting_Grid.title("Targeting grid")
Targeting_Grid.configure(bg = "black")

Columns = 9
Rows = 9
Buttons = []

print (str(floor(500/Columns)))

class grid_button:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        button = tk.Button(Targeting_Grid, command = self.on_click, text= (self.column + 1, self.row + 1))
        button.grid(row=row, column=column, sticky="nsew")

    def on_click(self):
        global cords
        cords = (f' Row: {str(self.row + 1)}  Column: {str(self.column + 1)}')
        print(F'Currently targeting {cords}')
        Fire.place(x=250, y=400, anchor="center")

def fire():
    print(f'Target {cords} locked. Firing!')

for column in range(Columns):
    Button_Column = []
    for row in range(Rows):
        button = grid_button(row, column)
        Button_Column.append(button)
    Buttons.append(Button_Column)

Fire = tk.Button(Targeting_Grid, command=fire, text = 'Fire')

tk.mainloop()