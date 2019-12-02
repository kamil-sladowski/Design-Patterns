class Product:
    modules = []

    def __init__(self, modules):
        self.modules = modules

    def printContainedModules(self):
        print(self.__class__.__name__)
        for module in self.modules:
            print(module.name)


class TV(Product): pass


class Toaster(Product): pass


class Peeler(Product): pass
