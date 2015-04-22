import logging
import StringIO

import requests

from .exception import (ConnectionRefused, HTTPError, )

log = logging.getLogger(__name__)

class DaapStringIO(StringIO.StringIO):
    """Subclass ```StringIO``` to use custom methods on StringIO instances"""

    def __init__(self, b):
        StringIO.StringIO.__init__(self, b)

    def get_data(self, n, start=0):
        """Read n bytes and replace the cursor to ```.tell() - n```"""
        if start > 0:
            self.seek(self.tell() + start)

        data = self.read(n)

        self.seek(self.tell() - (n + start))
        return data

class DaapRequest(object):
    """
    :param string pairing_code: DAAP pairing code client <-> server, see README
    :param string host: DAAP server host, default localhost
    :param int port: DAAP server port, default 3689

    Creates object to request our DAAP server.
    """
    def __init__(self, pairing_code=None, **kwargs):
        # DAAP pairing code
        self.pairing_code = pairing_code

        # DAAP server host
        self.host = host
        # DAAP server port
        self.port = port

        # DAAP mandatory headers
        self.headers = {'Viewer-Only-Client': '1'}

        # DAAP server URL
        self.server_url = 'http://{}:{}/'.format(self.host, self.port)

    def get(self, endpoint):
        """Make an HTTP request on the DAAP server.
        This method returns raw data
        """
        URL = '{}{}'.format(self.server_url, endpoint)

        log.debug('GET {}'.format(URL))
        log.debug('Headers: {}'.format(self.headers))

        try:
            resp = requests.get(URL, headers=self.headers)
        except requests.exceptions.ConnectionError:
            raise ConnectionRefused()

        if resp.status_code != 200:
            raise HTTPError('HTTP error {}'.format(resp.status_code))

        return DaapStringIO(resp.content)
