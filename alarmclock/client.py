import socket, time

FILE_NAME = "alarm_times.txt"
PORT = 2550
IP = "10.0.0.48"

def run(ip):
    print("Threading")
    print(ip, " ", PORT)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect(sock, (IP, PORT))
    while True:
        try:
            data = sock.recv(1024)
            if data == b'':
               print("Connection broken, reconnecting...")
               connect(sock, (IP, PORT))
            else:
               with open(FILE_NAME, 'w') as f:
                   time = data.decode("utf-8")
                   print("New Time: ", time)
                   f.write(time)
        except Exception as e:
            print(e)
            connect(sock, (IP, PORT))

def connect(sock, addr):
    connected = False
    print("connecting")
    print(addr)
    while not connected:
        try:
            sock.connect(addr)
            connected = True
            print("connected")
        except Exception as e:
            print("Failed to connect, retrying...")
            pass
        time.sleep(0.5)
