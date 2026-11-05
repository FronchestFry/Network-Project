#Server

import socket

host = socket.gethostbyname(socket.gethostname()) #Since this is the server, it just hosts on whatever adress it is on. Clients will have to type the target IP
port = 1578 #Chosen arbatrarily from anything above 1000

network_object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
network_object.bind((host, port))

print(f'Server launched. Clients will need to connect to the ip {host} and the port {port}.')

network_object.listen()

client_connection, client_adress = network_object.accept()

print(f"Connected to by {client_adress}")
client_connection.sendall(b"You have connected successfully")

while True:
#Echo to check connection
    #Recive data
    incoming_data = client_connection.recv(port)

    #Check that the client still exists
    if not incoming_data:
        print (f"client '{client_adress}' disconnected")
        break


#Handle the inbound data
    print(f"Oponent attacked square '{incoming_data.decode()}'")
    outgoing_data = input("Return fire at what cordinate?\n")
    print(f"Shot fired at '{outgoing_data}'. Awaiting enemy's return fire.")
    client_connection.sendall(outgoing_data.encode())
