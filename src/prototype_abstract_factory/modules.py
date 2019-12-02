import copy


class Module:
    def __call__(self):
        return copy.deepcopy(self)


class ModuleA(Module):
    name = "A"


class ModuleB(Module):
    name = "B"


class ModuleC(Module):
    name = "C"


class ModuleD(Module):
    name = "D"
