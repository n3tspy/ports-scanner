import sys
import socket

if len(sys.argv) > 1:
    hostname = sys.argv[1]
    try:
        ip = socket.gethostbyname(hostname)
        print(f"Adresse IP de {hostname} : {ip}")
    except socket.gaierror:
        print(f"Non resolution de l'hostname : {hostname}")
    
    ports = range(1, 1025)
    for port in ports:
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(5.0)
            connect = client.connect((ip, port))
            #print(f"Tentative de connexion au port : {port}")
            banner = client.recv(1024).decode().strip()
            print(f"Banner pour : {ip}:{port} -> {banner}")
        except:
            print(f"Connexion echoue")
        finally:
            client.close()