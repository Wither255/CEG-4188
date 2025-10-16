import socket

import socket

HOST = "0.0.0.0"
PORT = 53333
TARGET = b"hello TCP"
BATCH_SIZE = 1000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"TCP Server listening on {HOST}:{PORT}")

    conn, addr = server_socket.accept()
    with conn:
        print(f"Connected by {addr}")
        count = 0

        while True:
            data = conn.recv(8192)
            if not data:
                print("Client closed connection.")
                break
            found = data.count(TARGET)
            if found:
                count += found

            if count >= BATCH_SIZE:
                conn.sendall(b"back at you TCP")
                print("Replied after 1000 messages.")
                break   # Snippet for the 1000 message question
