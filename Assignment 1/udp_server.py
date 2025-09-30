import socket

HOST = "0.0.0.0"
PORT = 53444

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
    server_socket.bind((HOST, PORT))
    print(f"UDP Server listening on {HOST}:{PORT}")

    while True:
        data, addr = server_socket.recvfrom(1024)
        message = data.decode()
        print(f"Received from {addr}: {message}")
        if message == "hello UDP":
            server_socket.sendto("back at you UDP".encode(), addr)
