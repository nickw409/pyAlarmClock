import socket, time, os, select

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
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setblocking(False)
    
    addr = (IP, PORT)
    connect(sock, addr)
    curr_time = time.time()
    while True:
        try:
            if not writeable(sock):
                connect(sock, addr)
            else:
                if readable(sock):
                    #when recv time, send back mirror msg to confirm
                    data = sock.recv(1024)
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
            connected = writeable(sock)
            print("connected")
        except Exception as e:
            print("Failed to connect, retrying...")
            print(e)
        time.sleep(1)

def check_conn(sock):
    data = "hello there".encode("utf-8")
    sock.sendall(data)
    if readable(sock):
        recv_data = sock.recv(1024).decode("utf-8")
        


def writeable(sock):
    read_sock, write_sock, error = select.select(
        [], [sock], [], 60
    )
    if len(write_sock) > 0 and write_sock[0]:
        return True
    else:
        return False

def readable(sock):
    read_sock, write_sock, error = select.select(
        [sock], [], [], 60
    )
    if len(read_sock) > 0 and read_sock[0]:
        return True
    else:
        return False

