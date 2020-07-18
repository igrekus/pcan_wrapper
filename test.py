from PCANBasic import PCANBasic, TPCANMsg
from time import sleep

from ctypes import *

pcan = PCANBasic()

print('init')
pcan.Initialize(65, c_ushort(284), c_ubyte(1), 256, 3)

sleep(2)

print('ready msg')
msg = TPCANMsg()

msg.ID = 255
msg.LEN = 8
msg.MSGTYPE = 0

# for i, val in enumerate([252, 0, 3, 0, 0, 0, 0, 0]):
    # msg.DATA[i] = int(str(val))
    
data = [0, 0, 2, 0, 0, 0, 0, 0]
for i in range(8):
    msg.DATA[i] = data[i]

# msg.DATA = [] (c_ubyte * 8)(*[c_ubyte(d) for d in [1, 0, 2, 0, 0, 0, 0, 0]])

print(msg.ID)
print(msg.LEN)
print(msg.MSGTYPE)
print(msg.DATA, list(msg.DATA))

print('send msg')
result = pcan.Write(65, msg)
print('result', result)

sleep(3)

# for i, val in enumerate([0, 0, 2, 0, 0, 0, 0, 0]):
    # msg.DATA[i] = int(str(val), 16)

# msg.DATA = (c_ubyte * 8)(*[c_ubyte(d) for d in [0, 0, 2, 0, 0, 0, 0, 0]])

# pcan.Write(65, msg)

pcan.Uninitialize(65)
