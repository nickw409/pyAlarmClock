import socket, unittest, time, sys, os, threading, select
from queue import Queue
sys.path.append(os.path.abspath('../flaskr'))
import server

class TestServer(unittest.TestCase):
    def test01_socket_connection(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect((socket.gethostname(), 2550))
            self.assertTrue()
        except Exception as e:
            self.assertFalse()
        finally:
            sock.close()
    
    def test02_servertest01(self):
        #server.run()
        self.assertTrue()
    
    def test03_serverthreadtest01(self):
        server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_sock.setblocking(0)
        server_sock.bind((socket.gethostname(), 2550))
        server_sock.listen()

        q = Queue()

        t = threading.Thread(target=self.helpertest03)
        t.start()

        while True:
            read_sock, write_sock, error = select.select(
                [server_sock], [], [], 60
            )
            for sock in read_sock:
                if sock == server_sock:
                    print("Client connecting")
                    (client, addr) = server_sock.accept()
                    q.put(client)
        
        t.join()
    
    def helpertest03(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        time.sleep(1)
        try:
            sock.connect(("10.0.0.8", 2550))
            time.sleep(1)
        except Exception as e:
            print("Error connecting")
            sock.close()
            self.assertFalse()
        sock.close()



if __name__ == "__main__":
    unittest.main()