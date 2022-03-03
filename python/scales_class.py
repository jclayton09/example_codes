import serial
from time import sleep


class Scales(object):

    _baudrate = 2400
    _bytesize = serial.SEVENBITS
    _timeout = None
    _stopbits = serial.STOPBITS_ONE
    _parity = serial.PARITY_EVEN

    def __init__(self, port='/dev/ttyUSB0'):
        self.port = port

    def _query(self):
        with serial.Serial(port=self.port, baudrate=self._baudrate, bytesize=self._bytesize, timeout=self._timeout, stopbits=self._stopbits, parity=self._parity) as cheese:
            return cheese.read(size=46)

    def read(self):
        name = str(self._query()).replace(' ', '')
        split = name[2:44].split(',')
        print(len(name), len(split))
        print(name)
        if len(name) == 49 and len(split) == 6:
            print(f"{split[0]},weight={float(split[4])}, unit={split[5]}, header={split[3]}")
        else:
            print('Error')
            self.read()