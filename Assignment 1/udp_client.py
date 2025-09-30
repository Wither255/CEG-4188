import socket
import time

HOST = "127.0.0.1"
PORT = 53444

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
    print("Connected to UDP server.")

    client_socket.sendto("hello UDP".encode(), (HOST, PORT))
    data, _ = client_socket.recvfrom(1024)
    print("Server:", data.decode())

    while True:
        time.sleep(1)
