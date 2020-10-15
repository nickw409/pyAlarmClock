import socket, select, threading
from queue import Queue

def run():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.setblocking(0)
    server_sock.bind((socket.gethostname(), 2550))
    server_sock.listen()

    q = Queue()

    t = threading.Thread(target=threader, daemon=True, args=(q,))
    t.start()
    
    #use a nonblocking socket
    while True:
        read_sock, write_sock, error = select.select(
            [server_sock], [], [], 60
        )
        for sock in read_sock:
            if sock == server_sock:
                (client, addr) = server_sock.accept()
                q.put(client)

def threader(q):
    with open("alarm_time.txt", 'r') as f:
        settings = f.read()
    
    while True:
        sock = q.get()
        send_data(sock, settings)

def send_data(sock, settings):
    while writeable(sock):
        with open("alarm_time.txt" 'r') as f:
            new_settings = f.read()
            if settings != new_settings:
                settings = new_settings
                sock.sendall(settings)
    sock.close()
    q.task_done()
    

def writeable(sock):
    read_sock, write_sock, error = select.select(
        [], [sock], [], 60
    )
    for s in write_sock:
        if s == sock:
            return True