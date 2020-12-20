from ..Vulnerabilities.Remotecontrol import RemoteControl
from ..Vulnerabilities.Criticalerror import CriticalError
from ..Vulnerabilities.Phpinjection import PHPInjection
from ..Vulnerabilities.Sqlinjection import SQLInjection

class Device:
    """
    Базовый класс для всех устройств.
    """
    def __init__(self):
        self.name = None
        self.powered = False
        self.vulnerabilities = []

    def set_vulnerability(self, vulnerability):
        if vulnerability == "remotecontrol":
            vulnerability = RemoteControl()
        elif vulnerability == "criticalerror":
            vulnerability = CriticalError()
        elif vulnerability == "phpinjection":
            vulnerability = PHPInjection()
        elif vulnerability == "sqlinjection":
            vulnerability = SQLInjection()
        else:
            return 13
        if str(type(self)).split(".")[-1][:-2] not in vulnerability.devices:
            return 14
        self.vulnerabilities += [vulnerability]
        return 0

    def del_vulnerability(self, vulnerability):
        if vulnerability not in self.vulnerabilities:
            return 14
        del self.vulnerabilities[self.vulnerabilities.index(vulnerbility)]
        return 0

    def set_name(self, name):
        if self.name == name:
            return 8
        self.name = name
        return 0

    def power_on(self):
        """
        Включает устройство.
        :return: код ошибки
        """
        if self.powered:
            return 2
        self.powered = True
        return 0

    def power_off(self):
        """
        Выключает устройство.
        :return: код ошибки
        """
        if not self.powered:
            return 3
        self.powered = False
        return 0

    def send(self, to_address, data):
        pass

    def receive(self, from_address, packet):
        if packet.to_address == self.name:
            return [self.do(packet.data, packet), packet]
        if self.name in packet.trace:
            return [16, packet]
        packet.add_to_trace(self.name)
        return self.send(packet.to_address, packet=packet)

    def do(self, command):
        pass
