#Client

'''
NOTICE:

DUE TO VSCODE ISSUES, I NOW HAVE TO WRITE THE CODE IN HERE AND THEN RUN/TEST THROUGH THE PYTHON IDLE, INSTEAD OF VSCODE'S RUNNER. PLEASE FORGIVE ANY SLIGHT ODDITIES IN TIMING CAUSED BY THIS.

For some reason vscode is randomly adding "" arround my file names, causing it to look for a file that doesn't exist instead of the actual file I need to run.
'''



import socket

server_addr = input("Server IP:\n")
server_port = int(input("Server Port:\n"))

#Make the object that interacts with networks
network_object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Connect to the server
network_object.connect((server_addr, server_port))


#Recive the intro message
print (network_object.recv(server_port).decode())

#Run once manually to kick it off pre-loop

outgoing_data = input("Awaiting attack cordinates:\n")
if outgoing_data.lower() == "quit":
    network_object.close()
else:
    print(f"Shot fired at '{outgoing_data}'. Awaiting enemy's return fire.")
    network_object.sendall(outgoing_data.encode())

#Begin the standard loop
while not network_object._closed:
    #print recived data
    incoming_data = network_object.recv(server_port)
    if not incoming_data:
            print (f"Host '{server_addr}' disconnected.")
            break

    else: print(f"Opponent Returned Fire at '{incoming_data.decode()}'")

    #Get an input and send it to whomever I'm connected to
    outgoing_data = input("Awaiting attack cordinates:\n")
    if outgoing_data.lower() == "quit":
        network_object.close()
    else:
        print(f"Shot fired at '{outgoing_data}'. Awaiting enemy's return fire.")
        network_object.sendall(outgoing_data.encode())
