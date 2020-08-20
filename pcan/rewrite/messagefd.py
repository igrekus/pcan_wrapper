from ctypes import Structure, c_uint, c_ubyte


class CtypeMessageFD(Structure):
    """
    Represents a PCAN message from a FD capable hardware
    """
    _fields_ = [
        ("ID", c_uint),  # 11/29-bit message identifier
        ("MSGTYPE", c_ubyte),  # Type of the message
        ("DLC", c_ubyte),  # Data Length Code of the message (0..15)
        ("DATA", c_ubyte * 64)  # Data of the message (DATA[0]..DATA[63])
    ]


class MessageFD:
    """
    High-level wrapper around Ctype struct
    """

    def __init__(self, id, command, p_array):
        """
        :param id -- идентификатор подсистемы
        :param command -- команда, которую должна будет выполнить подсистема
        :param p_array -- массив параметров команды
        """
        self._id = id
        self._command = command
        self._p_array = p_array

        self._ctype_message = None

    def _build_message(self):
        self._ctype_message = CtypeMessageFD()
        self._ctype_message.ID = c_uint(self._id)
        self._ctype_message.LEN = c_ubyte(8)   # TODO calculate actual msg length based on MSGTYPE
        self._ctype_message.MSGTYPE = c_ubyte(0)

        # for i in range(8 if (theMsg.LEN > 8) else theMsg.LEN):
        #     newMsg.DATA[i] = theMsg.DATA[i]

        self._p_array = [self._command] + self._p_array
        for i, byte in enumerate(self._p_array):
            self._ctype_message.DATA[i] = c_ubyte(byte)

    @property
    def as_ctype(self):
        if self._ctype_message is None:
            self._build_message()
        return self._ctype_message
