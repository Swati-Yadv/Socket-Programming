import socket

def run_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = socket.gethostbyname(socket.gethostname())
    port = 4444     

    server.bind((server_ip, port))
    server.listen()
    print(f"Listening on {server_ip}:{port}")
    while True: 
        client_socket, client_address = server.accept()
        print(f"Accepted client_socket from {client_address}")

    # receiving data from client
        while True:
            request = client_socket.recv(2048)
            # converting bytes to string
            request = request.decode('utf-8')
            request = request.upper()
            print(request)
            if request.lower() == "close":
                print(request)
                client_socket.close()
                break
            else:
                client_socket.sendall(request.encode())
        client_socket.close()

run_server() 
