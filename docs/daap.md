### Daap module

## Daap

This class will usually be your entry point to Pydaap. It contains
every functions you need to interact with your DAAP server.

__class Daap([pairing_code=None, **kwargs])__

Create a new Daap object.

Most of the methods require pairing_code to be set. This can be
obtained by pairing your app with your DAAP server. I wrote a little
node.js application to pair your app with a DAAP server: 
[PairingJS](https://github.com/j-muller/PairingJS).

Some options can be defined but are not mandatory :

* `host` (default: `"127.0.0.1"`)
* `port` (default: `3689`)

__Daap.server_info(self)__

Returns info about the DAAP server.

__Daap.content_codes(self)__

Returns the instructions length and verbose name.