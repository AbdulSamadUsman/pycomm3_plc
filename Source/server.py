"""
PLC Server side class that receive tags and setup server side
"""
import os


class Server:
    """
    Class that uses CPPPO library to connect server
    """

    def __init__(self, plc_initialze):
        """
        Initilize parameters through dictionar
        Args:
         plc_initialze: Usse  dictionary argument which is a combination of
         tag with its size and datatype

         """
        self.plc_initialze = plc_initialze
        self.str_frmt = "enip_server --print"

    def connect(self):
        """
                    Function to connect PLC and show Status
        """
        print("Server is running with following Enable TAGS")
        for i in range(0, len(self.plc_initialze["TAG"])):
            self.str_frmt = self.str_frmt + "  " + self.plc_initialze["TAG"][i] + "=" +\
            self.plc_initialze["DATATYPE"][i] + "[" + str(self.plc_initialze["SIZE"][i]) + "]"
            print("TAG", i, self.plc_initialze["TAG"][i])
        os.system(self.str_frmt)
