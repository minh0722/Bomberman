import sys
# import queue
from socket import *
from game_settings import *
from network_socket import NetworkSocket
from threading import Thread
from util import encode, decode
from network_events import *
# from arena import Arena
# from player import Player


class Client:
    def __init__(self):
        self.socket = NetworkSocket()
        self.socket.connect(('localhost', PORT))

        self.is_connected = True

        self.socket.set_blocking(0)

        self.receive_thread = Thread()
        self.receive_thread.run = self._receive_packet_from_server
        self.receive_thread.start()

        self.send_packet(encode(Event.START))

        # self.arena = Arena()
        # self.players = list()
        # self.input_handler = None

        # self.incoming_packets = queue.Queue()

    def send_packet(self, packet):
        self.socket.send_all(packet)

    def connected(self):
        return self.is_connected

    def _get_event_list(self, packet):
        splitted_events = packet.split('.')

        splitted_events = list(filter(('.').__ne__, splitted_events))
        splitted_events = list(filter(('').__ne__, splitted_events))

        return splitted_events

    def _receive_packet_from_server(self):
        while True:
            try:
                packet = self.socket.recv()
                # print(packet)
                print(self._get_event_list(packet))

                if decode(packet) == Event.EXIT:
                    break

                elif decode(packet) == Event.SERVER_FULL:
                    print("Server full! Try again later!")
                    self.is_connected = False
                    break

                self.is_connected = True

            except Exception as e:
                pass

    def __del__(self):
        print("joining thread")
        self.receive_thread.join()
        self.socket.close_socket()