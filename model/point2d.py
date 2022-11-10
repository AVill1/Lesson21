import math


class Point2D:

    @staticmethod
    def sum(a,b):
        return a + b

    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    @x.deleter
    def x(self):
        del self._x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y

    @y.deleter
    def y(self):
        del self._y

    def calculate_distance(self, point):
        if not isinstance(point, Point2D):
            return -1

        return math.sqrt((self._x - point._x)**2 + (self._y-point._y)**2)


    def __str__(self):
        return f"Point ({self._x};{self._y})"