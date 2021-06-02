"""
The clients will communicate with the arbiter which will be the bottleneck in the communication
with the distributed shared memory. The arbiter will pass on the query to the distributed 
network or will deal with it on its own based on the type of the message that it gets.
"""

class Arbiter:

    def __init__(self):
        self.var_list = []

    @staticmethod
    def get_new_process_id():
        """
        Contactts the server to get the new node_id for a user wanting to connect
        """
        pass

    def send_shared_var(self, shared_var):
        """
        Contacts the server and sends the variable in serialized form so as to be set as shared
        """
        pass

    def get_all_shared_var(self):
        """

        """
        pass

    def get_var(self,shared_var):
        """
        Contacts the server to get the variable that is being requested for read replication
        """
        pass

    def get_write_access(self,shared_var):
        """
        Contacts the server to get write access for the given variable 
        """
        pass


    # def listen_for_changes(self):
    #     """
    #     The arbiter for each node will listen to the server so that when a node revokes
    #     shared status for a variable, it is trickled down
    #     """
    #     pass