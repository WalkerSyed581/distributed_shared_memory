from .config import *
from _thread import *
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
        self.node_id = self.subscribe()
        self.metadata = self.get_all_shared_var()
        self.client_shared_vars = None
        self.read_replicated_vars = None
        self.write_accessed = None
        self.client_sock = None
        self.write_lock = threading.Lock()        


    def subscribe(self):
        pass

    def __listen(self):
        pass

    def __send_message(self):
        pass

    def __parse_message(self):
        pass

    # When another client requests a variable read replicated by this one
    def __halt_read(self):
        pass

    def __update_metadata(self):
        pass



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