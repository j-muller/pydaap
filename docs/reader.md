### Reader module

The aim of this class is to convert RAW data (usually bytes list)
to understandable types. For example, convert 4 bytes to `int32`.

## DaapNumericReader

__class DaapNumericReader__

Convert bytes to numeric data. All the methods are `@classmethod`.

__DaapNumericReader.uint8(cls, b)__

Convert 1 byte to an unsigned big-endian number.

__DaapNumericReader.uint16(cls, b)__

Convert 2 bytes to an unsigned big-endian number.

__DaapNumericReader.uint32(cls, b)__

Convert 4 bytes to an unsigned big-endian number.

__DaapNumericReader.uint64(cls, b)__

Convert 8 bytes to an unsigned big-endian number.

__DaapNumericReader.int8(cls, b)__

Convert 1 byte to a signed big-endian number.

__DaapNumericReader.int16(cls, b)__

Convert 2 bytes to a signed big-endian number.

__DaapNumericReader.int32(cls, b)__

Convert 4 bytes to a signed big-endian number.

__DaapNumericReader.int64(cls, b)__

Convert 8 bytes to a signed big-endian number.
