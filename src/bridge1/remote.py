from src.bridge1.device import Device


class Remote:

    def __init__(self, device_instance: Device):
        self._device_instance = device_instance

    def togglePower(self):
        if self._device_instance.isEnabled():
            self._device_instance.disable()
        else:
            self._device_instance.enable()

    def volumeDown(self):
        self._device_instance.setVolume(0.25)

    def volumeUp(self):
        self._device_instance.setVolume(-0.25)

    def channelUp(self):
        self._device_instance.setNextChannel()