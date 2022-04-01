import math

class Auto:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def rep(self):
        return f'x: {self.x}; y:{self.y}'

    def move(self, dist):
        self.x = self.x + dist * math.cos(self.direction)
        self.y = self.y + dist * math.sin(self.direction)

    def turn_left(self):
        if self.direction < 90:
            self.direction = 360 + (self.direction - 90)
        else:
            self.direction -= 90

    def turn_right(self):
        if self.direction > 270:
            self.direction = 360 - (self.direction + 90)
        else:
            self.direction += 90

class Bus(Auto):
    def __init__(self, x, y, direction, people, mony):
        super().__init__(x, y, direction)
        self.people = people
        self.mony = mony

    def in_bus(self, fluctuation):
        self.people += fluctuation

    def out_bus(self, fluctuation):
        self.people -= fluctuation

    def collect_money(self, dist):
        self.move(dist)
        self.mony = dist * self.people
        return self.mony

bus = Bus(10, 10, 90, 5, 0)

bus.collect_money(1)
print(bus.rep())
print(bus.mony)

bus.collect_money(3)
print(bus.rep())
print(bus.mony)

bus.in_bus(1)
bus.collect_money(1)
print(bus.rep())
print(bus.mony)