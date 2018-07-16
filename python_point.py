import random


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Test():
    def __init__(self, string, nb):
        self.string = string
        self.points = []
        for i in range(nb):
            self.points.append(Point(random.random(), random.random()))
        self.distances = []

    def increment_string(self, n):
        tmp = ""
        for c in self.string:
            tmp += chr(ord(c) + n)
        self.string = tmp

    def distance_between_points(self):
        for i, a in enumerate(self.points):
            for b in self.points:
                self.distances.append(((b.x -a.x) **2 + (b.y -b.x)**2) ** 0.5)

if __name__ == '__main__':
    test = Test("A nice sentence to test.", 10000)
    test.increment_string(-5)
    test.distance_between_points()
