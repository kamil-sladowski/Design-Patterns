from src.bridge1.remote import Remote


class AdvancedRemote(Remote):
    def mute(self):
        self._device_instance.setVolume(0)
