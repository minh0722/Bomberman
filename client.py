import sys
import Queue
from socket import *
from game_settings import *
from network_socket import NetworkSocket
from threading import Thread
from util import encode
import time


class Client:
    def __init__(self):
        self.socket = NetworkSocket()
        self.socket.connect(('localhost', PORT))
        self.incoming_packets = Queue.Queue()
        self.outgoing_packets = Queue.Queue()
        self.game_over = False

        self.receive_packet_thread = Thread()
        self.receive_packet_thread.run = self._receive_packet_from_server
        self.receive_packet_thread.start()

        self.get_packet_thread = Thread()
        self.get_packet_thread.run = self._get_incoming_packet_from_queue
        self.get_packet_thread.start()

        self.send_packet_thread = Thread()
        self.send_packet_thread.run = self._send_outgoing_packet_from_queue
        self.send_packet_thread.start()

    # def __del__(self):
    #     self.receive_packet_thread.join()
    #     self.get_packet_thread.join()
    #     self.send_packet_thread.join()
    #     print("all joined")

    def exclusive_send_packet(self, packet):
        # send packet immediately without waiting in queue
        self.socket.send_all(packet)

    def send_packet(self, packet):
        self.outgoing_packets.put(packet, block=False)

    def set_game_over(self, is_game_over):
        self.game_over = is_game_over

    def _receive_packet_from_server(self):
        while True and not self.game_over:
            packet = self.socket.recv()
            if packet:
                self.incoming_packets.put(packet)

    def _send_outgoing_packet_from_queue(self):
        while True and not self.game_over:
            try:
                packet = self.outgoing_packets.get(block=False)
                # time.sleep(0.0001)
                self.socket.send_all(packet)
            except Queue.Empty:
                continue

    def _get_incoming_packet_from_queue(self):
        while True and not self.game_over:
            try:
                packet = self.incoming_packets.get(block=False)
                print("received packet: ", packet)
            except Queue.Empty:
                continue

    # def run_client(self):
    #     try:
    #         # Send data
    #         message = 'This is the message. It will be repeated'
    #         print('sending "%s"' % message)
    #         self.socket.send_all(message.encode('utf-8'))

    #         # Look for the response
    #         amount_received = 0
    #         amount_expected = len(message)

    #         while amount_received < amount_expected:
    #             data = self.socket.recv(16)
    #             amount_received += len(data)
    #             print('received "%s"' % data)

    #     finally:
    #         self.socket.close_socket()


# c = Client()

# for i in range(20):
#     c.send_packet("sd")

