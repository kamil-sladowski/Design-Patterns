import copy

from modules import *

class RobotPrototype:
    own_module = None

    def clone(self):
        return copy.copy(self)

    def createModule(self, times=1):
        modules_set = []
        for _ in range(times):
            modules_set.append(self.own_module.clone())
        return modules_set


class RobotA(RobotPrototype):

    def __init__(self):
        self.own_module = ModuleA()


class RobotB(RobotPrototype):

    def __init__(self):
        self.own_module = ModuleB()


class RobotC(RobotPrototype):

    def __init__(self):
        self.own_module = ModuleC()


class RobotD(RobotPrototype):

    def __init__(self):
        self.own_module = ModuleD()
