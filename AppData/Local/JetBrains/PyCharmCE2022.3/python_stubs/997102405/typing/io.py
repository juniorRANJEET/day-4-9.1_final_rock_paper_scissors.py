# encoding: utf-8
# module typing.io
# from C:\Program Files\Python310\DLLs\_asyncio.pyd
# by generator 1.147
""" Wrapper namespace for IO generic classes. """

# imports
import typing as __typing


# no functions
# classes

class IO(__typing.Generic):
    """
    Generic base class for TextIO and BinaryIO.
    
        This is an abstract, generic version of the return of open().
    
        NOTE: This does not distinguish between the different possible
        classes (text vs. binary, read vs. write vs. read/write,
        append-only, unbuffered).  The TextIO and BinaryIO subclasses
        below capture the distinctions between text vs. binary, which is
        pervasive in the interface; however we currently do not offer a
        way to track the other distinctions in the type system.
    """
    def close(self): # reliably restored by inspect
        # no doc
        pass

    def fileno(self): # reliably restored by inspect
        # no doc
        pass

    def flush(self): # reliably restored by inspect
        # no doc
        pass

    def isatty(self): # reliably restored by inspect
        # no doc
        pass

    def read(self, n=-1): # reliably restored by inspect
        # no doc
        pass

    def readable(self): # reliably restored by inspect
        # no doc
        pass

    def readline(self, limit=-1): # reliably restored by inspect
        # no doc
        pass

    def readlines(self, hint=-1): # reliably restored by inspect
        # no doc
        pass

    def seek(self, offset, whence=0): # reliably restored by inspect
        # no doc
        pass

    def seekable(self): # reliably restored by inspect
        # no doc
        pass

    def tell(self): # reliably restored by inspect
        # no doc
        pass

    def truncate(self, size=None): # reliably restored by inspect
        # no doc
        pass

    def writable(self): # reliably restored by inspect
        # no doc
        pass

    def write(self, s): # reliably restored by inspect
        # no doc
        pass

    def writelines(self, lines): # reliably restored by inspect
        # no doc
        pass

    def __enter__(self): # reliably restored by inspect
        # no doc
        pass

    def __exit__(self, type, value, traceback): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __orig_bases__ = (
        typing.Generic[~AnyStr],
    )
    __parameters__ = (
        None, # (!) real value is '~AnyStr'
    )
    __slots__ = ()


class BinaryIO(__typing.IO):
    """ Typed version of the return of open() in binary mode. """
    def write(self, s): # reliably restored by inspect
        # no doc
        pass

    def __enter__(self): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __orig_bases__ = (
        typing.IO[bytes],
    )
    __parameters__ = ()
    __slots__ = ()


class TextIO(__typing.IO):
    """ Typed version of the return of open() in text mode. """
    def __enter__(self): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    buffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    encoding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    errors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    line_buffering = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    newlines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __orig_bases__ = (
        typing.IO[str],
    )
    __parameters__ = ()
    __slots__ = ()


# variables with complex values

__all__ = [
    'IO',
    'TextIO',
    'BinaryIO',
]

__weakref__ = None # (!) real value is "<attribute '__weakref__' of 'typing.io' objects>"

