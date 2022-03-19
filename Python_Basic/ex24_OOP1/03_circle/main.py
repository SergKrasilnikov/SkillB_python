class Circle:
    pi = 3.14159

    def __init__(self, x=0, y=0, r=1):
        self.x = x
        self.y = y
        self.r = r

    def area(self):
        return self.r * self.r * self.pi

    def perimeter(self):
        return 2 * self.r * self.pi

    def scale(self, k):
        self.r *= k

    def intersect(self, other):
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2 <= (self.r + other.r) ** 2


circle_1 = Circle(0, 0, 1)
circle_2 = Circle(0, 0, 1)
circle_3 = Circle(55, 55, 1)

# ----------TESTS----------
print(circle_1.area())
circle_1.scale(2)
print(circle_1.area())
print(circle_1.intersect(circle_2))
print(circle_1.intersect(circle_3))

# зачёт!
