from socket import *
import sys
from game_settings import *
from network_socket import NetworkSocket

class Client:
    def __init__(self):
        self.socket = NetworkSocket()
        self.socket.connect(('localhost', PORT))

    def run(self):
        try:
            # Send data
            message = 'This is the message. It will be repeated'
            print('sending "%s"' % message)
            self.socket.send_all(message.encode('utf-8'))

            # Look for the response
            amount_received = 0
            amount_expected = len(message)

            while amount_received < amount_expected:
                data = self.socket.recv(16)
                amount_received += len(data)
                print('received "%s"' % data)

        finally:
            self.socket.close_socket()

c = Client()
c.run()
