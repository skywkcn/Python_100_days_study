from math import sqrt


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_to(self, x, y):
        self.x = x
        self.y = y
        return '(%s, %s)' % (str(self.x), str(self.y))

    def move_by(self, dx, dy):
        self.x += dx
        self.y += dy
        return '(%s, %s)' % (str(self.x), str(self.y))

    def distance_to(self, other):
        dw = self.x - other.x
        dh = self.y - other.y
        return sqrt(dw ** 2 + dh ** 2)



p1 = Point(2, 5)
p2 = Point(2, 5)
print(p1.move_to(5, 19))
print(p2.move_by(1, 1))
print(p1.distance_to(p2))
