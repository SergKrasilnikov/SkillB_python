class Figure:
    figure_name = 'Figure'

    def __init__(self, __figure_name: str):
        self.figure_name = __figure_name

class Square(Figure):
    def __init__(self, side: float):
        super().__init__('Squer')
        self.side = side

    def square_sq(self: any):
        return self.side ** 2

    def square_per(self: any):
        return 4 * self.side

class Triangle(Figure):
    def __init__(self, a, b, c):
        super().__init__('Triangle')
        self.a = a
        self.b = b
        self.c = c

    def triangle_sq(self):
        return self.a * self.b * self.c

    def triangle_per(self):
        return self.a + self.b + self.c

class Cube(Figure):
    def __init__(self, side):
        super().__init__('Cub')
        self.side = side

    def cub_sq(self):
        return 6 * (self.side ** 2)

class Pyramid(Figure):
    def __init__(self, side, high):
        super().__init__('Pyramid')
        self.side = side
        self.high = high

    def py_sq(self):
        return self.side * (self.side + (2 * self.high))

pyramid = Pyramid(2, 4)
print(pyramid.py_sq())
print(pyramid.figure_name)

cube = Cube(2)
print(cube.cub_sq())
print(cube.figure_name)

