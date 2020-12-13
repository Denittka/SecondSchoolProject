from ..Device import Device
from ..LAN import LAN
from ..USB import USB


class Computer(Device, LAN, USB):
    def __init__(self):
        super().__init__()
        self.usb_connected = []
        self.usb_connection_limit = None
        self.local_connected = []
        self.local_connection_limit = None

    def send(self):
        pass

    def receive(self):
        pass