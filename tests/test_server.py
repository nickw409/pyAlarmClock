import socket

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((socket.gethostname(), 2550))
        print("Socket connected")
    except Exception as e:
        print("There was an error connecting")
    finally:
        sock.close()

if __name__ == "__main__":
    main()