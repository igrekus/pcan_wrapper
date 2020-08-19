from ctypes import Structure, c_uint, c_ubyte


class CtypeMessage(Structure):
    """
    Represents a PCAN message
    """
    _fields_ = [
        ("ID", c_uint),  # 11/29-bit message identifier
        ("MSGTYPE", c_ubyte),  # Message type
        ("LEN", c_ubyte),  # Data Length Code of the message (0..8)
        ("DATA", c_ubyte * 8)  # Data of the message (DATA[0]..DATA[7])
    ]


class Message:
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
        self._ctype_message = CtypeMessage()
        self._ctype_message.ID = self._id
        self._ctype_message.LEN = 8
        self._ctype_message.MSGTYPE = 0

        self._p_array = [self._command] + self._p_array
        for i, byte in enumerate(self._p_array):
            self._ctype_message.DATA[i] = byte

    @property
    def as_ctype(self):
        if self._ctype_message is None:
            self._build_message()
        return self._ctype_message
