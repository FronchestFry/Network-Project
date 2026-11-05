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

host = socket.gethostbyname(socket.gethostname()) #Since this is the server, it just hosts on whatever adress it is on. Clients will have to type the target IP
port = 1567 #Chosen arbatrarily from anything above 1000

network_object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
network_object.bind((host, port))

print(f'Server launched. Clients will need to connect to the ip {host} and the port {port}.')

network_object.listen()

client_connection, client_adress = network_object.accept()

print(f"Connected to by {client_adress}")
client_connection.sendall(b"You have connected successfully")

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
    client_connection.sendall(cords.encode())
    await_return()

def await_return():
    incoming_data = client_connection.recv(port)
    if not incoming_data:
        print (f"Host '{client_adress}' disconnected.")
        shutdown()
    else: print(f"Opponent Returned Fire at '{incoming_data.decode()}'")
    Targeting_Grid.deiconify()
    Targeting_Grid.update()

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

incoming_data = client_connection.recv(port)
print(f"Oponent attacked square '{incoming_data.decode()}'")

tk.mainloop()