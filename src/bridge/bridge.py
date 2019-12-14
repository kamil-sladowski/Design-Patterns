from abc import ABCMeta, abstractmethod

NOT_IMPLEMENTED = "Not implemented."


class PolygonAPI:
    __metaclass__ = ABCMeta

    @abstractmethod
    def draw(self, x, y, radius):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def count_area(self, x):
        raise NotImplementedError(NOT_IMPLEMENTED)


class CircleAPI(PolygonAPI):
    def count_area(self, radius):
        return "Area of circle denotes: " + str(3.14 * radius * radius)

    def draw(self, x, y, radius):
        return "Circle at ({0}:{1}). Radius: {2}".format(x, y, radius)


class TriangleAPI(PolygonAPI):
    def count_area(self, x):
        return "Area of triangle denotes: " + str(x * x * 1.73 / 4)

    def draw(self, x, y, radius):
        return "Triangle at ({0}:{1}). Radius: {2}".format(x, y, radius)


class SquareAPI(PolygonAPI):
    def count_area(self, x):
        return "Area of square denotes: " + str(x * x)

    def draw(self, x, y, radius):
        return "Square at ({0}:{1}). Radius: {2}".format(x, y, radius)


class AbstractCalculator:
    __metaclass__ = ABCMeta

    polygon_api = None

    def __init__(self, polygon_api):
        self.polygon_api = polygon_api

    @abstractmethod
    def draw(self):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def count_area(self):
        raise NotImplementedError(NOT_IMPLEMENTED)


class Calculator(AbstractCalculator):
    def __init__(self, x, y, area_parameter, polygon_api):
        self.x = x
        self.y = y
        self.area_parameter = area_parameter
        super(Calculator, self).__init__(polygon_api)

    def draw(self):
        return self.polygon_api.draw(self.x, self.y, self.area_parameter)

    def count_area(self):
        return self.polygon_api.count_area(self.area_parameter)


class AdvancedCalculator:

    @staticmethod
    def calculate():
        calculator_implementations = [
            Calculator(1.0, 0.0, 10.0, CircleAPI()),
            Calculator(2.0, 1.0, 11.0, TriangleAPI()),
            Calculator(3.0, 1.0, 12.0, SquareAPI())
        ]

        for calculator in calculator_implementations:
            print(calculator.count_area())
            print(calculator.draw())


if __name__ == "__main__":
    AdvancedCalculator.calculate()
