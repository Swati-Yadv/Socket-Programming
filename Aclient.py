import socket

def run_client():
    # creating socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # getting server ip
    server_ip = socket.gethostbyname(socket.gethostname())
    server_port = 4444

    #establishing connection with server
    client.connect((server_ip, server_port))
     
    while True:
        msg = input("Enter message: ")
        if not msg:
            break
        client.sendall(msg.encode("utf-8"))

        # receive message from server
        response = client.recv(2048).decode("utf-8")
        if not response:
            break
        print(f"Received data from server: {response}")
        
run_client()
       
