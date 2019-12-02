from modules import *
from robots import *
from products import *

class RobotsFactory:
    robots = []

    def __init__(self):
        self.robots.append(RobotA())
        self.robots.append(RobotB())
        self.robots.append(RobotC())
        self.robots.append(RobotD())

    def cloneRobotA(self):
        return self.robots[0].clone()

    def createTv(self):
        a_modules = self.robots[0].createModule(times=3)
        b_modules = self.robots[1].createModule(times=2)
        c_modules = self.robots[2].createModule(times=1)
        a_modules.extend(b_modules)
        a_modules.extend(c_modules)
        return TV(a_modules)

    def createToaster(self):
        a1_modules = self.robots[0].createModule(times=1)
        b_modules = self.robots[1].createModule(times=3)
        a2_modules = self.robots[0].createModule(times=1)
        d_modules = self.robots[3].createModule(times=1)
        a1_modules.extend(b_modules)
        a1_modules.extend(a2_modules)
        a1_modules.extend(d_modules)
        return Toaster(a1_modules)

    def createPeeler(self):
        c_modules = self.robots[2].createModule(times=1)
        d1_modules = self.robots[3].createModule(times=1)
        a_modules = self.robots[0].createModule(times=1)
        d2_modules = self.robots[3].createModule(times=1)
        c_modules.extend(d1_modules)
        c_modules.extend(a_modules)
        c_modules.extend(d2_modules)
        return Peeler(c_modules)