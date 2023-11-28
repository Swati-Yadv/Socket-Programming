import socket

def run_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_ip = socket.gethostbyname(socket.gethostname())
    port = 4443

    # address = (host, port)
    server.bind((server_ip, port))

    while True:
        data, address = server.recvfrom(2048)
        data = data.decode("utf-8")

        if data == "close":
            print("Client disconnected!")
            break
        print(f"Client: {data}")

        data = data.upper()
        data = data.encode("utf-8")
        server.sendto(data, address)

    server.close()

run_server()