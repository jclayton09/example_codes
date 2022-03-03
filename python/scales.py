import serial
import json


def read():
    serialPort = serial.Serial(port="/dev/ttyUSB0",
                               baudrate=2400,
                               bytesize=serial.SEVENBITS,
                               timeout=None,
                               stopbits=serial.STOPBITS_ONE,
                               parity=serial.PARITY_EVEN, )

    serialPort.readline()
    jazz = str(serialPort.readline())[2:46].replace(' ', '').split(',')
    return jazz


"""
# This is in influxdb form
name = read()
if len(name) == 6:
    # print(name)
    print(f"{name[0]},weight={float(name[4])}, unit={name[5]}, header={name[3]}")
else:
    print('Error')
"""

# This is in json form
name = read()
if len(name) == 6:
    # print(name)
    dataframe = {'name': name[0], 'weight': float(name[4]), 'unit': name[5], 'header': name[3]}
    print(json.dumps(dataframe, indent=2))

else:
    print('Error')
