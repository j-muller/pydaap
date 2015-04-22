# Pydaap

Python library for parsing Apple DAAP protocol

## Basic usage

```
>>> import json
>>> from pydaap import Daap
>>> d = Daap() # will connect to default host and port
>>> print(json.dumps(d.content_codes(), indent=4))
{
    "dmap.contentcodesresponse": {
        "dmap.status": 200,
        "dmap.dictionary": {
            "dmap.contentcodesnumber": 1634030422,
            "dmap.contentcodesname": "com.apple.itunes.music-sharing-version",
            "dmap.contentcodestype": 5
        }
    }
}
```

## API

* [Daap](daap.md)
* [Parser](parser.md)
* [Reader](reader.md)
* [Request](request.md)
* [Exception](exception.md)

## Project architecture

        setup.py           # Basic Python setup.py
        pydaap/
            daap.py        # Contains all Pydaap methods you will probably use
            parser.py      # Contains RAW DAAP -> Python dict parser methods
            reader.py      # Useful to convert bytes to readable type
            request.py     # Contains the tools to make requests 
                           # on your DAAP server

## Todo

Unfortunately, Apple never wrote an official documentation about this
protocol. This project has been written by reading papers by people
interested about that (you can find these links below), and by trying
to understand what the official iPhone/iPad Remote application did.

That's why this project is quite slow to get some update. But, feel free
to send pull requests, I will read these very carefully. :)

* Improve DAAP parser (I never met any issues, but we never know)
* Add methods to interact with DAAP server

## External resources

This project has been developed thanks to previous work by other people.
Here is some of the links which inspired and helped me.

* [http://daap.sourceforge.net/index.html](http://daap.sourceforge.net/index.html)
* [http://dacp.jsharkey.org/](http://dacp.jsharkey.org/)
* [http://blog.mycroes.nl/2008/08/pairing-itunes-remote-app-with-your-own.html](http://blog.mycroes.nl/2008/08/pairing-itunes-remote-app-with-your-own.html)
* [http://jinxidoru.blogspot.fr/2009/06/itunes-remote-pairing-code.html](http://jinxidoru.blogspot.fr/2009/06/itunes-remote-pairing-code.html)
* [https://code.google.com/p/tunesremote-plus/](https://code.google.com/p/tunesremote-plus/)
* And some others I unfortunately forgot... :(

## License

```
MIT License
-----------

Copyright (c) 2015 Jeffrey Muller (http://jeffrey.muller.so/)
Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
```