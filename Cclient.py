import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = socket.gethostbyname(socket.gethostname())
PORT = 4443
client.connect((IP, PORT))
print("Client Connected!")
file1 = open('mypeer.txt', 'w')
while True:
    data = client.recv(2048)
    file1.writelines(data.decode('utf-8'))
    if not data:
        break

file1.close()

