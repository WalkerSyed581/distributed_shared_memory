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
        pass

    def subscribe(self):
        pass

    def set_as_shared(self):
        pass

    def remove_shared_status(self):
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

    def check_write_access(self,shared_var):
        """
        Checks the memory manager to make sure that the variable has read access
        """
        pass