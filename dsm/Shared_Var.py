
class Shared_Var():
    """
    docstring
    """
    def __init__(self,var_name,value):
        """
        docstring
        """
        self._var_name = var_name
        self._value = value
        self._can_write = False
        
    def get_var_name(self):
        """
        docstring
        """
        return self._var_name
    
    def get_value(self):
        """
        docstring
        """
        return self._value

    def get_can_write(self):
        """
        docstring
        """
        return self._can_write

    def set_value(self,value):
        """
        docstring
        """
        self._value = value      
    