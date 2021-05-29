"""
The aim of this class is it works in tandem with the arbiter and manages the memory
and the variable that one of the node has accessed and they will be accessed with 
the help of this class along with maintaining read replication and other 
synchronization based problems
"""

class MemoryManager:

    def __init__(self):
        self.shared_vars = {}

    def store_accessed_var(self, shared_var):
        """
        This method will take the variable that the user tried to access 
        """
        pass

    def remove_var(self,shared_var):
        """
        This method will remove the given variable from the list of the variables that
        have been accessed for read replication
        """
        pass

    def grant_write_acess(self):
        """
        This will allow the user to change the variable and also contact the arbiter to
        send the changes when done
        """
        pass