from ctypes import Structure, c_uint, c_ushort


class CtypeTimestamp (Structure):
    """
    Represents a timestamp of a received PCAN message
    Total Microseconds = micros + 1000 * millis + 0x100000000 * 1000 * millis_overflow
    """
    _fields_ = [
        ("millis", c_uint),  # Base-value: milliseconds: 0.. 2^32-1
        ("millis_overflow", c_ushort),  # Roll-overs of millis
        ("micros", c_ushort)  # Microseconds: 0..999
    ]


class Timestamp:
    """
    High-level wrapper around Ctype struct
    """
    def __init__(self, millis, millis_overflow, micros):
        self._millis = millis
        self._millis_overflow = millis_overflow
        self._micros = micros

        self._ctype_timestamp: CtypeTimestamp = None

    def _build_timestamp(self):
        self._ctype_timestamp = CtypeTimestamp()
        self._ctype_timestamp.millis = c_uint(self._millis)
        self._ctype_timestamp.millis_overflow = c_ushort(self._millis_overflow)
        self._ctype_timestamp.micros = c_ushort(0)

    @property
    def as_ctype(self):
        if self._ctype_timestamp is None:
            self._build_timestamp()
        return self._ctype_timestamp
