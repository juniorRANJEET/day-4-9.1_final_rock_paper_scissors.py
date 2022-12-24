# encoding: utf-8
# module _overlapped
# from C:\Program Files\Python310\DLLs\_overlapped.pyd
# by generator 1.147
# no doc
# no imports

# Variables with simple values

ERROR_IO_PENDING = 997

ERROR_NETNAME_DELETED = 64

ERROR_OPERATION_ABORTED = 995

ERROR_PIPE_BUSY = 231

ERROR_SEM_TIMEOUT = 121

INFINITE = 4294967295

INVALID_HANDLE_VALUE = 18446744073709551615

NULL = 0

SO_UPDATE_ACCEPT_CONTEXT = 28683

SO_UPDATE_CONNECT_CONTEXT = 28688

TF_REUSE_SOCKET = 2

# functions

def BindLocal(*args, **kwargs): # real signature unknown
    """
    Bind a socket handle to an arbitrary local port.
    
    family should be AF_INET or AF_INET6.
    """
    pass

def ConnectPipe(*args, **kwargs): # real signature unknown
    """ Connect to the pipe for asynchronous I/O (overlapped). """
    pass

def CreateEvent(*args, **kwargs): # real signature unknown
    """
    Create an event.
    
    EventAttributes must be None.
    """
    pass

def CreateIoCompletionPort(*args, **kwargs): # real signature unknown
    """ Create a completion port or register a handle with a port. """
    pass

def FormatMessage(*args, **kwargs): # real signature unknown
    """ Return error message for an error code. """
    pass

def GetQueuedCompletionStatus(*args, **kwargs): # real signature unknown
    """
    Get a message from completion port.
    
    Wait for up to msecs milliseconds.
    """
    pass

def PostQueuedCompletionStatus(*args, **kwargs): # real signature unknown
    """ Post a message to completion port. """
    pass

def RegisterWaitWithQueue(*args, **kwargs): # real signature unknown
    """ Register wait for Object; when complete CompletionPort is notified. """
    pass

def ResetEvent(*args, **kwargs): # real signature unknown
    """ Reset event. """
    pass

def SetEvent(*args, **kwargs): # real signature unknown
    """ Set event. """
    pass

def UnregisterWait(*args, **kwargs): # real signature unknown
    """ Unregister wait handle. """
    pass

def UnregisterWaitEx(*args, **kwargs): # real signature unknown
    """ Unregister wait handle. """
    pass

def WSAConnect(*args, **kwargs): # real signature unknown
    """ Bind a remote address to a connectionless (UDP) socket. """
    pass

# classes

class Overlapped(object):
    """ OVERLAPPED structure wrapper. """
    def AcceptEx(self, *args, **kwargs): # real signature unknown
        """ Start overlapped wait for client to connect. """
        pass

    def cancel(self, *args, **kwargs): # real signature unknown
        """ Cancel overlapped operation. """
        pass

    def ConnectEx(self, *args, **kwargs): # real signature unknown
        """
        Start overlapped connect.
        
        client_handle should be unbound.
        """
        pass

    def ConnectNamedPipe(self, *args, **kwargs): # real signature unknown
        """ Start overlapped wait for a client to connect. """
        pass

    def DisconnectEx(self, *args, **kwargs): # real signature unknown
        pass

    def getresult(self, *args, **kwargs): # real signature unknown
        """
        Retrieve result of operation.
        
        If wait is true then it blocks until the operation is finished.  If wait
        is false and the operation is still pending then an error is raised.
        """
        pass

    def ReadFile(self, *args, **kwargs): # real signature unknown
        """ Start overlapped read. """
        pass

    def ReadFileInto(self, *args, **kwargs): # real signature unknown
        """ Start overlapped receive. """
        pass

    def TransmitFile(self, *args, **kwargs): # real signature unknown
        """ Transmit file data over a connected socket. """
        pass

    def WriteFile(self, *args, **kwargs): # real signature unknown
        """ Start overlapped write. """
        pass

    def WSARecv(self, *args, **kwargs): # real signature unknown
        """ Start overlapped receive. """
        pass

    def WSARecvFrom(self, *args, **kwargs): # real signature unknown
        """ Start overlapped receive. """
        pass

    def WSARecvInto(self, *args, **kwargs): # real signature unknown
        """ Start overlapped receive. """
        pass

    def WSASend(self, *args, **kwargs): # real signature unknown
        """ Start overlapped send. """
        pass

    def WSASendTo(self, *args, **kwargs): # real signature unknown
        """ Start overlapped sendto over a connectionless (UDP) socket. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    address = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Address of overlapped structure"""

    error = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Error from last operation"""

    event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Overlapped event handle"""

    pending = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether the operation is pending"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000027790C08850>'

__spec__ = None # (!) real value is "ModuleSpec(name='_overlapped', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000027790C08850>, origin='C:\\\\Program Files\\\\Python310\\\\DLLs\\\\_overlapped.pyd')"

