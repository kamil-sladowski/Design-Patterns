from RobotsFactory import *
from modules import *
from robots import *
from products import *

class DevicesFactory:

    def __init__(self):
        self.factory = RobotsFactory()

    def createProduct(self, product_type):
        if product_type == TV.__name__:
            return self.factory.createTv()
        elif product_type == Toaster.__name__:
            return self.factory.createToaster()
        else:
            return self.factory.createPeeler()