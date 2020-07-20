from pcan.PCANBasic import PCANBasic, TPCANMsg
from time import sleep

from ctypes import *

CHAN_ID = 65
BAUDRATE = c_ushort(284)
HW_TYPE = c_ubyte(1)
IO_PORT = 256
INTERRUPT = 3
pcan = PCANBasic()


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
pcan.Initialize(CHAN_ID, BAUDRATE, HW_TYPE, IO_PORT, INTERRUPT)

sleep(1)

print('ready message')
msg = build_message(id=255, command=1, p_array=[0, 2, 0, 0, 0, 0, 0])

print('send message')
result = pcan.Write(65, msg)

print('PCAN release')
pcan.Uninitialize(65)
