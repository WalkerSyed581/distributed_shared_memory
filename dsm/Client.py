from .config import *
from _thread import *
import socket
import threading

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
        Read Replicated Vars structure: {node_id: [variable_names]}
        Write Replicated Vars structure: {node_id: [variable_names]}
        """
        self.client_sock = None
        self.write_lock = threading.Lock()   
        self.node_id = self.subscribe()
        self.metadata = self.get_all_shared_var()
        self.client_shared_vars = None
        self.read_replicated_vars = None
        self.write_accessed = None     


    def subscribe(self):
        self.client_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server_addr = (IP,PORT)
        try:
            self.client_sock.connect(server_addr)
        except socket.error as e:
            print(str(e))
            
        self.client_sock.send(str.encode(self.__create_message(0)))

        recv_data = self.client_sock.recv(1024)

        if not recv_data:
           print("Unable to connect")

        
        response = str.decode(recv_data)
        response = str.split('|')
        node_id = self.__parse_message(response)
        return node_id
        
    def __listen(self):
        pass

    def __send_message(self):
        pass

    def __parse_message(self,message):
        

    # When another client requests a variable read replicated by this one
    def __halt_read(self):
        pass

    def __update_metadata(self):
        pass

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

    def set_as_shared(self,var):
        pass

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
        pass

    def check_write_access(self,shared_var):
        """
        Checks the memory manager to make sure that the variable has read access
        """
        pass