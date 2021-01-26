from src.bridge1.device import Device


class TV(Device):

    def __init__(self):
        super().__init__()
        self.brightness = 0.5

    def setBrightness(self, brightness):
        self.brightness += brightness