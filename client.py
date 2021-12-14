#import socket module
import socket
server  = '10.0.0.10'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
#create TCP/IP socket
s = socket.socket()
#get user input ip server
#server = input('please enter a ip ')
#bind the socket
s.connect((server, PORT))
#recieve message from server succsesfuly established
data = s.recv(1024).decode("utf-8")
print(server + ":" + data)

while True:
    #send message to server
    new_data = str(input("You: ")).encode("utf-8")
    s.sendall(new_data)
    # receive message from server
    data = s.recv(1024).decode("utf-8")
    print(server + ": " + data)

# close connection
s.close()