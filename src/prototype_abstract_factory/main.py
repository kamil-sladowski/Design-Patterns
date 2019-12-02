import copy
from modules import *
from robots import *
from products import *
from DevicesFactory import *





if __name__ == "__main__":
    factory = DevicesFactory()
    tv = factory.createProduct(TV.__name__)
    toaster = factory.createProduct(Toaster.__name__)
    peeler = factory.createProduct(Peeler.__name__)
    tv.printContainedModules()
    toaster.printContainedModules()
    peeler.printContainedModules()
