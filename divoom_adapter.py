import divoom_protocol
import divoom_device

class DivoomAdapter:

    def __init__(self, addr):
        self.protocol = divoom_protocol.DivoomAuraBoxProtocol()
        self.device = divoom_device.DivoomDevice(addr)

    def __enter__(self):
        self.device.connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.device.disconnect()