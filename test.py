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
        return self._can.Write(self._chan, message)

    def close(self):
        self._can.Uninitialize(self._chan)


def build_message(id, command, p_array):
    """
    :param id -- идентификатор подсистемы
    :param command -- команда, которую должна будет выполнить подсистема
    :param p_array -- массив параметров команды
    """
    message = TPCANMsg()

    message.ID = id
    message.LEN = 8
    message.MSGTYPE = 0

    p_array = [command] + p_array
    for i in range(8):
        message.DATA[i] = p_array[i]

    return message


print('PCAN init')
can = PCan()

sleep(1)

print('ready message')
msg = build_message(id=255, command=1, p_array=[0, 2, 0, 0, 0, 0, 0])

print('send message')
can.send(msg)

print('PCAN release')
can.close()
