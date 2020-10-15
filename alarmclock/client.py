import socket

FILE = "alarm_times.txt"

def run(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect(sock, (ip, port))
    while True:
        time = sock.recv()
        if time == b'':
            print("Connection broken, reconnecting...")
            connect(sock, (ip, port))
        else:
            with open(FILE, 'w') as f:
                f.write(time)

def connect(sock, addr):
    connected = False
    while not connected:
        try:
            sock.connect(addr)
            connected = True
        except Exception as e:
            pass
