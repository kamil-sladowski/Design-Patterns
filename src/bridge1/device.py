from itertools import cycle

class Device:

    _channels = cycle([1,2,3,4,5])

    def __init__(self):
        self.is_enabled = False
        self.volume = 0
        self.channel = next(Device._channels)

    def isEnabled(self):
        return self.is_enabled

    def enable(self):
        self.is_enabled = True

    def disable(self):
        self.is_enabled = False

    def getVolume(self):
        return self.volume

    def setVolume(self, percentage):
        self.volume += percentage

    def getChannel(self):
        return self.channel

    def setNextChannel(self):
        self.channel = next(Device._channels)