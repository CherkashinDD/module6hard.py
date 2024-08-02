import math


class Figure:
    sides_count = 0

    def __init__(self, __color, *sides):
        self.__color = list(__color)
        self.__sides = list(sides)
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else:
            print('Такого цвета нет')

    def __is_valid_sides(self, *new_sides):
        self.sides_ = []
        for side in new_sides:
            if isinstance(side, int) and side > 0:
                self.sides_.append(side)
        if len(self.sides_) == len(self.__sides):
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        self.new_sides = list(new_sides)
        if len(self.new_sides) == self.sides_count:
            self.__sides = self.new_sides

    def test_sides_count(self):
        if len(self.get_sides()) != self.sides_count:
            sides_ = [self.get_sides()[0]] * self.sides_count
            self.set_sides(*sides_)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__height = self.__calculate_height()

    def __calculate_height(self):
        a = self.get_sides()[0]
        b = self.get_sides()[1] if len(self.get_sides()) >= self.sides_count else self.get_sides()[0]
        c = self.get_sides()[2] if len(self.get_sides()) >= self.sides_count else self.get_sides()[0]
        p = sum(self.get_sides()) / 2
        return 2 * math.sqrt(p * (p - a) * (p - b) * (p - c)) / a

    def get_square(self):
        return (self.get_sides()[0] * self.__height) / 2


class Cube(Figure):
    sides_count = 12

    def __init(self, color, *sides):
        super().__init__(color, *sides)
        # sides_c = sides[0] *self.sides_count это моя крайняя попытка изменить __sides, изменить не получается
        # self.set_sides(sides_c)

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10, 15)
circle1.test_sides_count()

cube1 = Cube((222, 35, 130), 6)
cube1.test_sides_count()

triangle1 = Triangle((20, 5, 250), 30, 30)
triangle1.test_sides_count()

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

print(triangle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(f"Периметр круга: {len(circle1)}")

# Проверка объёма (куба):
print(f"Объём куба: {cube1.get_volume()}")

# Проверка площади треугольника
print(f"Площадь треугольника:{round(triangle1.get_square(), 2)}")
