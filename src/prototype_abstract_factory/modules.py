import copy


class Module:
    def __call__(self):
        return copy.deepcopy(self)

    def clone(self):
        return copy.copy(self)


class ModuleA(Module):
    name = "A"


class ModuleB(Module):
    name = "B"


class ModuleC(Module):
    name = "C"


class ModuleD(Module):
    name = "D"
