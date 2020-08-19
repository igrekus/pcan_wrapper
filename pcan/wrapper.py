from pcan.PCANBasic import PCANBasic, TPCANMsg
from time import sleep

from ctypes import *


class PCan:
    def __init__(self, chan=0x41, baudrate=0x11C, hw_type=0x1, io_port=0x100, interrupt=0x3):
        self._chan = chan

        self._can = PCANBasic()
        self._can.Initialize(
            Channel=chan,
            Btr0Btr1=c_ushort(baudrate),
            HwType=c_ubyte(hw_type),
            IOPort=c_uint(io_port),
            Interrupt=c_ushort(interrupt)
        )

    def send(self, message):
        return self._can.Write(self._chan, message.as_ctype)

    def close(self):
        self._can.Uninitialize(self._chan)


class Message:
    def __init__(self, id, command, p_array):
        """
        :param id -- идентификатор подсистемы
        :param command -- команда, которую должна будет выполнить подсистема
        :param p_array -- массив параметров команды
        """
        self._id = id
        self._command = command
        self._p_array = p_array

        self._tpcan_message = None

    def _build_message(self):
        self._tpcan_message = TPCANMsg()
        self._tpcan_message.ID = self._id
        self._tpcan_message.LEN = 8
        self._tpcan_message.MSGTYPE = 0

        self._p_array = [self._command] + self._p_array
        for i, byte in enumerate(self._p_array):
            self._tpcan_message.DATA[i] = byte

    @property
    def tpcan_message(self):
        if self._tpcan_message is None:
            self._build_message()
        return self._tpcan_message


if __name__ == '__main__':
    print('PCAN init')
    can = PCan()

    sleep(1)

    print('ready message')
    msg = Message(id=255, command=1, p_array=[0, 2, 0, 0, 0, 0, 0])

    print('send message')
    can.send(msg)

    print('PCAN release')
    can.close()
