import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = socket.gethostbyname(socket.gethostname())
PORT = 4443

server.bind((IP, PORT))

server.listen()
print(f"Listening on {IP}:{PORT}")
while True:
    connection, address = server.accept()
    try:
        print(f"Accepted client socket from {address}")

        while True:
            file1 = open('peer.txt', 'r')
            Lines = file1.readlines()
            for line in Lines: 
                connection.sendall(line.encode("utf-8"))
            connection.close()
            break
    
    finally:
        connection.close()


