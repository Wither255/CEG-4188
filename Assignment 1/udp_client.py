import socket

HOST = "127.0.0.1"
PORT = 53444

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
    client_socket.sendto("hello UDP".encode(), (HOST, PORT))
    data, _ = client_socket.recvfrom(1024)
    print("Received from server:", data.decode())
