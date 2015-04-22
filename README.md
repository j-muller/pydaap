Pydaap
======

[![Documentation Status](https://readthedocs.org/projects/pydaap/badge/?version=latest)](https://readthedocs.org/projects/pydaap/?badge=latest)

You can read the full documentation here: [http://pydaap.readthedocs.org/en/latest/](http://pydaap.readthedocs.org/en/latest/).

Pydaap is a python package to interact with DAAP servers. DAAP is
a protocol created by Apple and used in iTunes for example (so, you
can control your iTunes from your Python code). 

Feel free to fork this, it has been done to do this. :-)

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