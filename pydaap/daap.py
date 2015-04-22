import logging

from .request import DaapRequest
from .parser import DaapParser

class Daap(object):
    """ A Daap object.

    :param string pairing_code: DAAP pairing code client <-> server, see README
    :param string host: DAAP server host
    :param int port: DAAP server port

    This class creates a DAAP object to request our DAAP server.
    """
    def __init__(self, pairing_code=None, **kwargs):
        # DAAP pairing code
        self.pairing_code = pairing_code

        # DAAP server host
        self.host = kwargs.get('host', '127.0.0.1')
        # DAAP server port
        self.port = kwargs.get('port', 3689)

        # Request object
        self.req = DaapRequest(self.pairing_code, self.host, self.port)

    def server_info(self):
        resp = self.req.get('server-info')

        return DaapParser.parse(resp)

    def content_codes(self):
        resp = self.req.get('content-codes')

        return DaapParser.parse(resp)
