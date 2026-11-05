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

import socket

server_addr = input("Server IP:\n")
server_port = int(input("Server Port:\n"))

#Make the object that interacts with networks
network_object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Connect to the server
network_object.connect((server_addr, server_port))


#Recive the intro message
print (network_object.recv(server_port).decode())

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


def send_cords(cords):
    Fire.place_forget()
    Targeting_Grid.withdraw()
    print(f"Shot fired at '{cords}'. Awaiting enemy's return fire.")
    network_object.sendall(cords.encode())
    await_return()


def await_return():
    incoming_data = network_object.recv(server_port)
    if not incoming_data:
        print (f"Host '{server_addr}' disconnected.")
        shutdown()
    elif not network_object._closed:
        print(f"Opponent Returned Fire at '{incoming_data.decode()}'")
        Targeting_Grid.deiconify()
        Targeting_Grid.update()
    else:
        pass

def fire():
    send_cords(cords)

def shutdown():
    network_object.close()
    quit()

Targeting_Grid.protocol("WM_DELETE_WINDOW", shutdown)

for column in range(Columns):
    Button_Column = []
    for row in range(Rows):
        button = grid_button(row, column)
        Button_Column.append(button)
    Buttons.append(Button_Column)

Fire = tk.Button(Targeting_Grid, command=fire, text = 'Fire')

tk.mainloop()