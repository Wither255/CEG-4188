import socket

HOST = "0.0.0.0"   
PORT = 53333

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"TCP Server listening on {HOST}:{PORT}")

    conn, addr = server_socket.accept()
    with conn:
        print(f"Connected by {addr}")
        data = conn.recv(1024).decode()
        print("Received from client:", data)
        if data == "hello TCP":
            conn.sendall("back at you TCP".encode())
