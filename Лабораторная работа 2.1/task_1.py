import doctest

# TODO Написать 3 класса с документацией и аннотацией типов

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()  # тестирование примеров, которые находятся в документации

class House:
    def __init__(self, apartments: int, occupied_apartments: int, color: str):
        """
        Создание и подготовка к работе объекта "Дом"

        :param apartments: Количество квартир в доме
        :param occupied_apartments: Заселенные квартиры
        :param color: Цвет дома

        Примеры:
        >>> house = House(500, 200, "red")  # инициализация экземпляра класса
        """
        if not isinstance(apartments, int):
            raise TypeError("Количество квартир должно быть int")
        if apartments <= 0:
            raise ValueError("Количество квартир должно быть положительным числом")
        self.apartments = apartments

        if not isinstance(apartments, int):
            raise TypeError("Количество заселенных квартир должно быть int")
        if occupied_apartments < 0:
            raise ValueError("Количество заселенных квартир не может быть отрицательным числом")
        if occupied_apartments > apartments:
            raise ValueError("Количество заселенных квартир не может быть больше числа самих квартир")
        self.occupied_apartments = occupied_apartments

        if not isinstance(color, str):
            raise TypeError("Цвет дома должен быть типа str")
        self.color = color

    def rent_apartment(self, number_apartments_delivered) -> None:
        """
        Функция которая увеличивает количество заселенных квартир
        :param number_apartments_delivered: Количество купленных квартир

        Примеры:
        >>> house = House(500, 200, "red")
        >>> house.rent_apartment(300)
       """
        if not isinstance(number_apartments_delivered, int):
            raise TypeError("Количество купленных квартир должно быть int")
        if number_apartments_delivered + self.occupied_apartments > self.apartments:
            raise ValueError("Сумма заселенных квартир и купленных квартир не должна быть больше числа квартир")
        if number_apartments_delivered < 0:
            raise ValueError("Количество купленных квартир не может быть отрицательным числом")
        ...

    def repaint_house(self, new_color) -> None:
        """
        Перекрашивание дома

        :param new_color: Новый цвет дома

        Примеры:
        >>> house = House(500, 200, "red")
        >>> house.repaint_house("black")
        """
        ...
        if not isinstance(new_color, str):
            raise TypeError("Цвет дома должен быть типа str")
        ...

class Dog:
    def __init__(self, name: str, breed: str, age: int):
        """
        Создание и подготовка к работе объекта "Собака"

        :param name: Имя собаки
        :param breed: Порода собаки
        :param age: Возраст собаки

        Примеры:
        >>> dog = Dog("Ralf", "Bulldog", 3)  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Имя должно быть str")
        self.name = name

        if not isinstance(breed, str):
            raise TypeError("Порода должна быть str")
        self.breed = breed

        if not isinstance(age, int):
            raise TypeError("Возраст должен быть типа int")
        if age <= 0:
            raise TypeError("Возраст должен быть положительным числом")
        self.age = age

    def celebrate_birthday(self) -> None:
        """
        Функция которая увеличивает возраст собаки на один год
        :param number_apartments_delivered: Количество купленных квартир

        Примеры:
        >>> dog = Dog("Ralf", "Bulldog", 3)
        >>> dog.celebrate_birthday()
        """
        ...

    def information(self) -> str:
        """
        Получение информации о собаке

        :return: Имя, Порода, Возраст

        Примеры:
        >>> dog = Dog("Ralf", "Bulldog", 3)
        >>> dog.information()
        """
        ...


class Car:
    def __init__(self, current_fuel: int, tank_size: int, color: str):
        """
        Создание и подготовка к работе объекта "Машина"

        :param current_fuel: Текущее топливо
        :param tank_size: Размер бака
        :param color: Цвет машины

        Примеры:
        >>> car = Car(20, 60, "black")  # инициализация экземпляра класса
        """
        if not isinstance(current_fuel, int):
            raise TypeError("Количество топлива должно быть int")
        if current_fuel < 0:
            raise ValueError("Количество топлива не может быть отрицательным числом")
        self.current_fuel = current_fuel

        if not isinstance(tank_size, int):
            raise TypeError("Размер бака должен быть int")
        if tank_size <= 0:
            raise ValueError("Размер бака должен быть положительным числом")
        self.tank_size = tank_size

        if current_fuel > tank_size:
            raise ValueError("Текущее количество топлива превышает размер бака")

        if not isinstance(color, str):
            raise TypeError("Цвет должен быть str")
        self.color = color

    def refueling(self, filled_fuel: int) -> None:
        """
        Функция, которая увеличивает текущее топливо в машине
        :param filled_fuel: Количество топлива, готового к заправке

        Примеры:
        >>> car = Car(20, 60, "black")
        >>> car.refueling(20)
        """
        if filled_fuel + self.current_fuel > self.tank_size:
            raise ValueError("В машину заправлено топливо превышающее размер бака")
        ...

    def change_color(self, new_color) -> None:
        """
        Функция, которая меняет цвет машины
        :param new_color: Новый цвет машины

        Примеры:
        >>> car = Car(20, 60, "black")
        >>> car.change_color("orange")
        """
        if not isinstance(new_color, str):
            raise TypeError("Цвет должен быть str")
        self.color = new_color
        ...