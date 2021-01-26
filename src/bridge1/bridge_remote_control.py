from src.bridge1.AdvancedRemote import AdvancedRemote
from src.bridge1.TV import TV
from src.bridge1.remote import Remote

if __name__ == "__main__":
    tv = TV()
    remote = Remote(tv)
    advancedRemote = AdvancedRemote(tv)
    remote.togglePower()
    remote.channelUp()
    remote.channelUp()



