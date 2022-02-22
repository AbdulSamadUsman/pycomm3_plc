from pycomm3 import LogixDriver


class Client:

    def __init__(self, plc_initialize, plc_tags):
        self.ip = plc_initialize['ip']
        self.slot = plc_initialize['slot']
        self.client_plc = LogixDriver(self.ip, init_tags=False)
        self.client_plc._tags = plc_tags
        print(self.client_plc.tags)
        self.client_plc.open()
        self.info = self.client_plc.get_plc_info()
        print(self.info)
        self.client_plc.close()

    def write_tag(self, tag, value):
        self.client_plc.open()
        wr1 = self.client_plc.write(tag, value)
        print(wr1)
        self.client_plc.close()

    def read_tag(self, tag):
        self.client_plc.open()
        ret = self.client_plc.read(tag)
        print(ret)
        self.client_plc.close()

