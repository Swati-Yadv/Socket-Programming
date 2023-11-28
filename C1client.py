import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 4444

    # creating socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, PORT))

print("Client connected!")
file1 = open("cmdres.txt", "w")
user_input = str(input())
client.sendall(user_input.encode())
while True:
    data = client.recv(2048)
    file1.writelines(data.decode("utf-8"))
    if not data:
        break
file1.close()        
       
