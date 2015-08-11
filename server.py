from socket import *
import sys
from game_settings import *
from network_socket import NetworkSocket
from util import decode


class Server:
    def __init__(self):
        self.socket = NetworkSocket()
        self.socket.bind(('localhost', PORT))

    def run(self):
        self.socket.listen(MAX_CONNECTION)

        while True:
            print('waiting for a connection')
            connection_socket, client_address = self.socket.accept()
            print("connection established with ", client_address[0])

            try:
                while True:
                    data = connection_socket.recv(MAX_DATA_LEN)
                    print('received ', data)
                    new_data = decode(data)
                    new_data = new_data.split(' ')
                    print(new_data[0])

                    connection_socket.sendall("asdaqwe".encode('utf-8'))

                    if decode(data) == 'exit':
                        break
                    # if data:
                    # else:
                    #     break
            except Exception as e:
                print(e)
            finally:
                connection_socket.close()
                print("closing server connection socket")

    def __del__(self):
        self.socket.close_socket()

s = Server()
s.run()
