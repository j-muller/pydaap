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
    def __init__(self, pairing_code, host='127.0.0.1', port=3689):
        # DAAP server host
        self.host = host
        # DAAP server port
        self.port = port
        # DAAP pairing code
        self.pairing_code = pairing_code

        # Request object
        self.req = DaapRequest(self.pairing_code, self.host, self.port)

    def server_info(self):
        resp = self.req.get('server-info')

        import json

        print json.dumps(DaapParser.parse(resp), indent=4)

    def content_codes(self):
        resp = self.req.get('content-codes')

        import json

        print json.dumps(DaapParser.parse(resp), indent=4)