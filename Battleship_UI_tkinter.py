#I'm unsure which to use, I'll just try both until one hits a roadblock

import tkinter as tk

Targeting_Grid = tk.Tk()

Targeting_Grid.geometry("500x500")
Targeting_Grid.title("Targeting grid")
Targeting_Grid.configure(bg = "black")

Columns = 9
Rows = 9
Buttons = []


class grid_button:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        button = tk.Button(Targeting_Grid, command = self.on_click, text= (self.column + 1, self.row + 1))
        button.grid(row=row, column=column)

    def on_click(self):
        global cords
        cords = (f' Row: {str(self.row + 1)}  Column: {str(self.column + 1)}')
        print(F'Currently targeting {cords}')
        Fire.place(x=250, y=400, anchor="center")

def fire():
    print(f'Target {cords} locked. Firing!')

for column in range(Columns):
    label = tk.Label(text=column)
    label.grid()
    Button_Column = []
    for row in range(Rows):
        button = grid_button(row, column)
        Button_Column.append(button)
    Buttons.append(Button_Column)

Fire = tk.Button(Targeting_Grid, command=fire, text = 'Fire')

tk.mainloop()