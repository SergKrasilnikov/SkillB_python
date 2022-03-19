class Water:
    def __str__(self):
        return 'Water'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Wapor()
        elif isinstance(other, Soil):
            return Dirt()


class Air:
    def __str__(self):
        return 'Air'

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Light()
        elif isinstance(other, Soil):
            return Dust()
        else:
            return None


class Fire:
    def __str__(self):
        return 'Fire'

    def __add__(self, other):
        if isinstance(other, Water):
            return Wapor()
        elif isinstance(other, Air):
            return Light()
        elif isinstance(other, Soil):
            return Lawa()
        else:
            return None


class Soil:
    def __str__(self):
        return 'Soil'

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lawa()
        else:
            return None


class Storm:
    def __str__(self):
        return 'Storm'


class Wapor:
    def __str__(self):
        return 'Wapor'


class Dirt:
    def __str__(self):
        return 'Dirt'


class Light:
    def __str__(self):
        return 'Light'


class Dust:
    def __str__(self):
        return 'Dust'


class Lawa:
    def __str__(self):
        return 'Lawa'


water = Water()
air = Air()
fire = Fire()
soil = Soil()

print(water + air, '\n', water + fire, '\n', fire + soil, '\n', fire + air, '\n', air + air)

# зачёт!
