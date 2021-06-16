from _thread import *
import socket
import threading
import json
import sys
import random

from .Shared_Var import Shared_Var
from .config import *

"""
Implement the server side of the algorithm with the responsibility of managing 
incoming requests from the server and storing it on nodes according to an algorithm 
and passing the message to other clients that the data is available to be read
"""

class Server:
    def __init__(self):
        """
        var_data structure : {node_id: [Shared_Var]}
        """
        self.write_lock = threading.Lock()
        self.var_data = {}
        self.server_sock = None
        self.listen_sock = None
        self.write_lock = threading.Lock()   
        self._node_id = self.subscribe()
        self.get_all_shared_var()
        self.client_shared_vars = {}
        self.read_replicated_vars = {}
        self.listen_thread = threading.Thread(target=self.__listen)

    def __listen_client(self):
        """
        docstring
        """
        self.client_listen_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            self.client_listen_sock.bind(IP,ARBITER_PORT)
        except socket.error as e:
            print(str(e))

        self.client_listen_sock.listen(CLIENTS_LIMIT)

        while True:
            client, address = self.client_listen_sock.accept()
            start_new_thread(self.__threaded_client_listen,(client,address ))

    def __threaded_client_listen(self,client_conn,client_address):
        while True:
            request = client_conn.recv(BUFFER_SIZE)
            if not request:
                break
            if not self.__parse_incoming_client_request(request,client_address):
                self.send_request_to_client("-1|Unable to send request to server",client_address)

    

    