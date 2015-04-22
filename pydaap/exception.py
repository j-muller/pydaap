class ConnectionRefused(Exception):
    """Raised when the server does not handle the request"""

class HTTPError(Exception):
    """Raised when the DAAP server HTTP code status != 200
    It seems that a DAAP server should always returns 200.
    """

class DmapFieldNotFound(Exception):
    """Raised when DMAP field type extracted from buffer is not implemented
    """
