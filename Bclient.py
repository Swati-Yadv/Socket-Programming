import socket

def run_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_ip = socket.gethostbyname(socket.gethostname())
    port = 4443
    address = (server_ip, port)

    while True:
        data = input("Enter a word: ")
        if data == "close":
            data = data.encode("utf-8")
            client.sendto(data, address)
            print("Disconnected from the server.")
            break

        data = data.encode("utf-8")
        client.sendto(data, address)
        data, address = client.recvfrom(2048)
        data = data.decode("utf-8")
        print(f"Server: {data}")
    client.close()

run_client()