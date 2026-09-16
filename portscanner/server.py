import socket

HOST = "127.0.0.1"
PORT = 1000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"En écoute sur {HOST}:{PORT}...")

while True:
    conn, addr = server.accept()
    print(f"Connexion reçue de {addr}")
    conn.sendall(b"SSH-2.0-FakeServer_1.0\r\n")
    conn.close()