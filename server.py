from socket import *
import sys
from game_settings import *
from network_socket import NetworkSocket


class Server:
    def __init__(self):
        self.socket = NetworkSocket()
        self.socket.bind(('localhost', PORT))

    def run(self):
        self.socket.listen(MAX_CONNECTION)

        while True:
            print('waiting for a connection')
            connection_socket, client_address = self.socket.accept()

            try:
                # Receive data in small chunks and retransmit it
                while True:
                    data = connection_socket.recv(MAX_DATA_LEN)
                    print('received ', data)

                    # if data:
                    #     break
                    # if data:
                    #     connection_socket.sendall("a".encode('utf-8'))
                    # else:
                    #     break
            finally:
                connection_socket.close()
                print("closing server connection socket")

    def __del__(self):
        self.socket.close_socket()

s = Server()
s.run()
