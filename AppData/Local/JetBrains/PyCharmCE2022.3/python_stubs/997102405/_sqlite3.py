# encoding: utf-8
# module _sqlite3
# from C:\Program Files\Python310\DLLs\_sqlite3.pyd
# by generator 1.147
# no doc

# imports
import sqlite3 as __sqlite3


# Variables with simple values

PARSE_COLNAMES = 2
PARSE_DECLTYPES = 1

SQLITE_ALTER_TABLE = 26

SQLITE_ANALYZE = 28
SQLITE_ATTACH = 24

SQLITE_CREATE_INDEX = 1
SQLITE_CREATE_TABLE = 2

SQLITE_CREATE_TEMP_INDEX = 3
SQLITE_CREATE_TEMP_TABLE = 4
SQLITE_CREATE_TEMP_TRIGGER = 5
SQLITE_CREATE_TEMP_VIEW = 6

SQLITE_CREATE_TRIGGER = 7
SQLITE_CREATE_VIEW = 8
SQLITE_CREATE_VTABLE = 29

SQLITE_DELETE = 9
SQLITE_DENY = 1
SQLITE_DETACH = 25
SQLITE_DONE = 101

SQLITE_DROP_INDEX = 10
SQLITE_DROP_TABLE = 11

SQLITE_DROP_TEMP_INDEX = 12
SQLITE_DROP_TEMP_TABLE = 13
SQLITE_DROP_TEMP_TRIGGER = 14
SQLITE_DROP_TEMP_VIEW = 15

SQLITE_DROP_TRIGGER = 16
SQLITE_DROP_VIEW = 17
SQLITE_DROP_VTABLE = 30

SQLITE_FUNCTION = 31
SQLITE_IGNORE = 2
SQLITE_INSERT = 18
SQLITE_OK = 0
SQLITE_PRAGMA = 19
SQLITE_READ = 20
SQLITE_RECURSIVE = 33
SQLITE_REINDEX = 27
SQLITE_SAVEPOINT = 32
SQLITE_SELECT = 21
SQLITE_TRANSACTION = 22
SQLITE_UPDATE = 23

sqlite_version = '3.37.2'

version = '2.6.0'

# functions

def adapt(*args, **kwargs): # real signature unknown
    """ Adapt given object to given protocol. """
    pass

def complete_statement(*args, **kwargs): # real signature unknown
    """ Checks if a string contains a complete SQL statement. """
    pass

def connect(database, timeout=None, detect_types=None, isolation_level=None, check_same_thread=None, factory=None, cached_statements=None, uri=None): # real signature unknown; restored from __doc__
    """
    connect(database[, timeout, detect_types, isolation_level,
            check_same_thread, factory, cached_statements, uri])
    
    Opens a connection to the SQLite database file *database*. You can use
    ":memory:" to open a database connection to a database that resides in
    RAM instead of on disk.
    """
    pass

def enable_callback_tracebacks(*args, **kwargs): # real signature unknown
    """ Enable or disable callback functions throwing errors to stderr. """
    pass

def enable_shared_cache(*args, **kwargs): # real signature unknown
    """
    Enable or disable shared cache mode for the calling thread.
    
    This method is deprecated and will be removed in Python 3.12.
    Shared cache is strongly discouraged by the SQLite 3 documentation.
    If shared cache must be used, open the database in URI mode using
    the cache=shared query parameter.
    """
    pass

def register_adapter(*args, **kwargs): # real signature unknown
    """ Registers an adapter with sqlite3's adapter registry. """
    pass

def register_converter(*args, **kwargs): # real signature unknown
    """ Registers a converter with sqlite3. """
    pass

# classes

class Connection(object):
    """ SQLite database connection object. """
    def backup(self, *args, **kwargs): # real signature unknown
        """ Makes a backup of the database. """
        pass

    def close(self, *args, **kwargs): # real signature unknown
        """ Closes the connection. """
        pass

    def commit(self, *args, **kwargs): # real signature unknown
        """ Commit the current transaction. """
        pass

    def create_aggregate(self, *args, **kwargs): # real signature unknown
        """ Creates a new aggregate. """
        pass

    def create_collation(self, *args, **kwargs): # real signature unknown
        """ Creates a collation function. """
        pass

    def create_function(self, *args, **kwargs): # real signature unknown
        """ Creates a new function. """
        pass

    def cursor(self, *args, **kwargs): # real signature unknown
        """ Return a cursor for the connection. """
        pass

    def enable_load_extension(self, *args, **kwargs): # real signature unknown
        """ Enable dynamic loading of SQLite extension modules. """
        pass

    def execute(self, *args, **kwargs): # real signature unknown
        """ Executes an SQL statement. """
        pass

    def executemany(self, *args, **kwargs): # real signature unknown
        """ Repeatedly executes an SQL statement. """
        pass

    def executescript(self, *args, **kwargs): # real signature unknown
        """ Executes multiple SQL statements at once. """
        pass

    def interrupt(self, *args, **kwargs): # real signature unknown
        """ Abort any pending database operation. """
        pass

    def iterdump(self, *args, **kwargs): # real signature unknown
        """ Returns iterator to the dump of the database in an SQL text format. """
        pass

    def load_extension(self, *args, **kwargs): # real signature unknown
        """ Load SQLite extension module. """
        pass

    def rollback(self, *args, **kwargs): # real signature unknown
        """ Roll back the current transaction. """
        pass

    def set_authorizer(self, *args, **kwargs): # real signature unknown
        """ Sets authorizer callback. """
        pass

    def set_progress_handler(self, *args, **kwargs): # real signature unknown
        """ Sets progress handler callback. """
        pass

    def set_trace_callback(self, *args, **kwargs): # real signature unknown
        """ Sets a trace callback called for each SQL statement (passed as unicode). """
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __enter__(self, *args, **kwargs): # real signature unknown
        """
        Called when the connection is used as a context manager.
        
        Returns itself as a convenience to the caller.
        """
        pass

    def __exit__(self, *args, **kwargs): # real signature unknown
        """
        Called when the connection is used as a context manager.
        
        If there was any exception, a rollback takes place; otherwise we commit.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    DatabaseError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DataError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Error = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IntegrityError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    InterfaceError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    InternalError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    in_transaction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    isolation_level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    NotSupportedError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    OperationalError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ProgrammingError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    row_factory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    text_factory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    total_changes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Warning = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class Cursor(object):
    """ SQLite database cursor class. """
    def close(self, *args, **kwargs): # real signature unknown
        """ Closes the cursor. """
        pass

    def execute(self, *args, **kwargs): # real signature unknown
        """ Executes an SQL statement. """
        pass

    def executemany(self, *args, **kwargs): # real signature unknown
        """ Repeatedly executes an SQL statement. """
        pass

    def executescript(self, *args, **kwargs): # real signature unknown
        """ Executes multiple SQL statements at once. """
        pass

    def fetchall(self, *args, **kwargs): # real signature unknown
        """ Fetches all rows from the resultset. """
        pass

    def fetchmany(self, *args, **kwargs): # real signature unknown
        """
        Fetches several rows from the resultset.
        
          size
            The default value is set by the Cursor.arraysize attribute.
        """
        pass

    def fetchone(self, *args, **kwargs): # real signature unknown
        """ Fetches one row from the resultset. """
        pass

    def setinputsizes(self, *args, **kwargs): # real signature unknown
        """ Required by DB-API. Does nothing in sqlite3. """
        pass

    def setoutputsize(self, *args, **kwargs): # real signature unknown
        """ Required by DB-API. Does nothing in sqlite3. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        """ Implement next(self). """
        pass

    arraysize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    connection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lastrowid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rowcount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    row_factory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class Error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class DatabaseError(__sqlite3.Error):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class DataError(__sqlite3.DatabaseError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class IntegrityError(__sqlite3.DatabaseError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class InterfaceError(__sqlite3.Error):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class InternalError(__sqlite3.DatabaseError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class NotSupportedError(__sqlite3.DatabaseError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class OperationalError(__sqlite3.DatabaseError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class PrepareProtocol(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class ProgrammingError(__sqlite3.DatabaseError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class Row(object):
    # no doc
    def keys(self, *args, **kwargs): # real signature unknown
        """ Returns the keys of the row. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass


class Warning(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

adapters = {
    (
        None, # (!) real value is "<class 'datetime.date'>"
        PrepareProtocol,
    ): 
        None # (!) real value is '<function register_adapters_and_converters.<locals>.adapt_date at 0x0000023499EED5A0>'
    ,
    (
        None, # (!) real value is "<class 'datetime.datetime'>"
        '<value is a self-reference, replaced by this string>',
    ): 
        None # (!) real value is '<function register_adapters_and_converters.<locals>.adapt_datetime at 0x0000023499EED630>'
    ,
}

converters = {
    'DATE': None, # (!) real value is '<function register_adapters_and_converters.<locals>.convert_date at 0x0000023499EEE200>'
    'TIMESTAMP': None, # (!) real value is '<function register_adapters_and_converters.<locals>.convert_timestamp at 0x0000023499EEE290>'
}

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000023499D38850>'

__spec__ = None # (!) real value is "ModuleSpec(name='_sqlite3', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000023499D38850>, origin='C:\\\\Program Files\\\\Python310\\\\DLLs\\\\_sqlite3.pyd')"

