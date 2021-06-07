from .config import *
from _thread import *
import socket
import threading
import json

"""
The client side is the part of the network that requests and subscribes to the network
and uses the DSM functionality. This class will provide the functionality that will help
the user to just create this class and be able so subscribe directly to the DSM. This
class will use both the Aribter and Memory Manager class so as to allow the subscribing
to the network and specifying what to share and what to access in tandem with the other
two classes.
"""

class Client:
    def __init__(self):
        """
        Metadata structure : {node_id: [variable_names]}
        Read Replicated Vars structure: {node_id: {variable_names : value}}
        Write Replicated Vars structure: {node_id: [variable_names]}
        """
        self.client_sock = None
        self.listen_sock = None
        self.write_lock = threading.Lock()   
        self.node_id = self.subscribe()
        self.metadata = self.get_all_shared_var()
        self.client_shared_vars = None
        self.read_replicated_vars = None
        self.write_accessed = None
        self.listen_thread = threading.Thread(target=self.__listen)

    def subscribe(self):
        self.client_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server_addr = (IP,SERVER_PORT)
        try:
            self.client_sock.connect(server_addr)
        except socket.error as e:
            print(str(e))
            
        self.__send_message(str.encode(self.__create_message(0)))

        recv_data = self.client_sock.recv(1024)

        if not recv_data:
           print("Unable to connect")

        
        node_id = self.__parse_response(response)
        return node_id

    def __threaded_client_listen(self,server_conn):
        while True:
            request = server_conn.recv(4096)
            if not request:
                break
            self.__parse_incoming_request(request)
        connection.close()

    def __listen(self):
        self.listen_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            self.listen_sock.bind(IP,CLIENT_PORT)
        except socket.error as e:
            print(str(e))

        self.listen_sock.listen(1)

        while True:
            server, address = self.listen_sock.accept()
            start_new_thread(self.__threaded_client_listen,(server, ))

    def __send_message(self,encoded_message):
        self.client_sock.send(encoded_message)

    def __parse_response(self,message):
        response = str.decode(message)
        response = str.split('|')
        msg_type = int(response[0])
        if msg_type == -1:
            print(response[1])
            del self
        elif msg_type == 0:
            return int(response[1])
        elif msg_type == 1:
            
        elif msg_type == 2:

        elif msg_type == 3:

        elif msg_type == 4:
            if response[2] == '':
                print("No vairables have been shared")
                return None
            else:    
                return json.load(response[2])
            
        elif msg_type == 5:

        elif msg_type == 6:

        elif msg_type == 7:

    def __parse_incoming_request(self,message):
        request = str.decode(message)
        request = str.split('|')
        msg_type = int(request[0])
        if msg_type == -1:
            print(request[1])
            del self
        elif msg_type == 0:
            if self.node_id == int(reponse[1]):
                self.__halt_read(target_node_id,var_name): 
            else:
                return
        elif msg_type == 1:
            if self.node_id == int(reponse[1]):
                self.__update_metadata(response[2]): 
            else:
                return

    # When another client requests write access to a variable read replicated by this one
    def __halt_read(self,target_node_id,var_name):
        if target_node_id in self.read_replicated_vars and 
            request[3] in self.read_replicated_vars[target_node_id]:
            self.read_replicated_vars[target_node_id].pop(var_name)

    def __update_metadata(self,json_string):
        self.metadata = json.load(json_string)

    def __create_message(self,message_id,args=None):
        message = None
        if message_id == 0:
            message = "0"
        elif message_id == 1:
            message = "1|{}|{}|{}".format(str(args.node_id),str(args.var_name),str(args.value))
        elif message_id == 2:
            message = "2|{}|{}".format(str(args.node_id),str(args.var_name))
        elif message_id == 3:
            message = "3|{}|{}|{}".format(str(args.node_id),str(args.traget_node_id),str(args.var_name))
        elif message_id == 4:
            message = "4|{}".format(str(args.node_id))
        elif message_id == 5:
            message = "5|{}|{}|{}".format(str(args.node_id),str(args.traget_node_id),str(args.var_name))
        elif message_id == 6:
            message = "6|{}|{}|{}".format(str(args.node_id),str(args.traget_node_id),str(args.var_name))
        elif message_id == 7:
            message = "7|{}|{}|{}".format(str(args.node_id),str(args.traget_node_id),str(args.var_name))
        
        return message

    def set_as_shared(self,var_name,value):
        self.__send_message(self.__create_message(1,{node_id:self.node_id,}))


    def remove_shared_status(self,var):
        pass

    def get_var(self,shared_var):
        """
        This method gets a single variable from the ones that have been shared to the 
        server for reading
        """
        pass

    def get_write_access(self,shared_var):
        """
        This method gets the variable from the server to allow the node to be able to 
        change it for at the server level
        """
        pass

    def revoke_write_access(self,shared_var):
        pass

    def get_all_shared_var(self):
        """

        """
        self.__send_message(str.encode(self.__create_message(4,args={node_id:self.node_id})))
        recv_data = self.client_sock.recv(4096)

        if not recv_data:
           print("Unable to connect")

        
        self.metadata = self.__parse_response(recv_data)


    def check_write_access(self,shared_var):
        """
        Checks the memory manager to make sure that the variable has read access
        """
        pass