from modules import *

class RobotPrototype:
    own_module = None

    def clone(self):
        pass

    def createModule(self, times=1):
        pass

    def createModule(self, times=1):
        modules_set = []
        for _ in range(times):
            new_module = self.own_module()
            modules_set.append(new_module)
        return modules_set


class RobotA(RobotPrototype):

    def __init__(self):
        self.own_module = ModuleA()

    def clone(self):
        return copy.copy(self)


class RobotB(RobotPrototype):

    def __init__(self):
        self.own_module = ModuleB()

    def clone(self):
        return copy.copy(self)


class RobotC(RobotPrototype):

    def __init__(self):
        self.own_module = ModuleC()

    def clone(self):
        return copy.copy(self)


class RobotD(RobotPrototype):

    def __init__(self):
        self.own_module = ModuleD()

    def clone(self):
        return copy.copy(self)
