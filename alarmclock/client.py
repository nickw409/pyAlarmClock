import socket, time, os

script_dir = os.path.dirname(os.path.realpath(__file__))
FILE_NAME = os.path.join(script_dir, "alarm_times.txt")
PORT = 27550
#IP = "10.0.0.48"
IP = "34.217.124.84"

def run(ip):
    print("Threading")
    print(FILE_NAME)
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
            print(e)
            pass
        time.sleep(0.5)
