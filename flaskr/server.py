import socket, select, threading, time
from queue import Queue

if __name__ == "__main__":
    FILE_NAME = "../alarm_time.txt"
else:
    FILE_NAME = "alarm_time.txt"

def run():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.setblocking(0)
    server_sock.bind(('', 2550))
    server_sock.listen(5)

    q = Queue()

    t = threading.Thread(target=threader, daemon=True, args=(q,))
    t.start()
    
    #use a nonblocking socket
    while True:
        read_sock, write_sock, error = select.select(
            [server_sock], [], [], 1
        )
        if len(read_sock) > 0 and read_sock[0]:
            #print("incoming connection")
            (client, addr) = server_sock.accept()
            q.put(client)
        #else:
            #print("waiting")

def threader(q):
    with open(FILE_NAME, 'r') as f:
        data = f.read()
        #print("threader")
    while True:
        sock = q.get()
        send_data(sock, data, q)

def send_data(sock, data, q):
    #print("send_data")
    while writeable(sock):
        with open(FILE_NAME, 'r') as f:
            new_data = f.read()
            if data != new_data:
                data = new_data
                encoded_data = data.encode("utf-8")
                try:
                    sock.sendall(encoded_data)
                except Exception as e:
                    break
        time.sleep(0.3)
    sock.close()
    q.task_done()

def writeable(sock):
    read_sock, write_sock, error = select.select(
        [], [sock], [], 60
    )
    if len(write_sock) > 0 and write_sock[0]:
        return True
    else:
        return False

if __name__ == "__main__":
    run()