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
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            print("Received from client:", data)
            if data.lower() == "hello tcp":
                conn.sendall("back at you TCP".encode())
            else:
                conn.sendall(f"Echo: {data}".encode())
