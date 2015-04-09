import struct

class DaapNumericReader(object):
    """This class reads raw DAAP data and convert it to number
    """

    @classmethod
    def uint8(cls, b):
        """Read 1 byte, then convert to an unsigned big-endian number
        """
        n, = struct.unpack('>B', b)

        return n

    @classmethod
    def uint16(cls, b):
        """Read 2 bytes, then convert to an unsigned big-endian number
        """
        n, = struct.unpack('>H', b)

        return n

    @classmethod
    def uint32(cls, b):
        """Read 4 bytes, then convert to an unsigned big-endian number
        """
        n, = struct.unpack('>I', b)

        return n

    @classmethod
    def uint64(cls, b):
        """Read 8 bytes, then convert to an unsigned big-endian number
        """
        n, = struct.unpack('>Q', b)

        return n

    @classmethod
    def int8(cls, b):
        """Read 1 byte, then convert to a signed big-endian number
        """
        n, = struct.unpack('>b', b)

        return n

    @classmethod
    def int16(cls, b):
        """Read 2 bytes, then convert to a signed big-endian number
        """
        n, = struct.unpack('>h', b)

        return n

    @classmethod
    def int32(cls, b):
        """Read 4 bytes, then convert to a signed big-endian number
        """
        n, = struct.unpack('>i', b)

        return n

    @classmethod
    def int64(cls, b):
        """Read 8 bytes, then convert to a signed big-endian number
        """
        n, = struct.unpack('>q', b)

        return n
