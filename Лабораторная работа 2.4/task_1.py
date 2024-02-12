class Animal:
    """
    Животные - базовый класс.
    """

    def __init__(self, species: str, age: int):
        """
        Конструктор класса Animal.

        :param species: Вид животного.
        :param age: Возраст животного.
        """
        self.species = species
        self.age = age

    def __str__(self) -> str:
        """
        Магический метод для получения строкового представления объекта.

        :return: Строковое представление объекта.
        """
        return f"вид: {self.species}, возраст: {self.age}"

    def __repr__(self) -> str:
        """
        Магический метод для получения представления объекта.

        :return: Представление объекта.
        """
        return f"{self.__class__.__name__}(species='{self.species}', age={self.age})"

    def return_age(self) -> str:
        """
        Метод для получения возраста животного.

        :return: Строка с возрастом животного.
        """
        return f"Возраст животного: {self.age} лет"

    def return_species(self) -> str:
        """
        Метод для получения вида животного.

        :return: Строка с видом животного.
        """
        return f"Вид животного: {self.species}"


class Turtle(Animal):
    """
    Дочерний класс для черепах.
    """
    def __init__(self, species: str, age: int, color: str):
        """
        Конструктор класса Turtle.

        :param species: Вид животного.
        :param age: Возраст животного.
        :param color: Цвет панциря черепахи.
        """
        super().__init__(species, age)
        self.color = color

    def __str__(self) -> str:
        """
        Перегрузка магического метода для получения строкового представления объекта.

        :return: Строковое представление объекта.
        """
        return f"вид: {self.species}, цвет: {self.color}, возраст: {self.age}"

    def return_age(self) -> str:
        """
        Перегрузка метода получения возраста черепахи.

        :return: Строка с возрастом черепахи.
        """
        return  f"Возраст черепахи: {self.age} лет"


if __name__ == "__main__":
    animal_1 = Animal("млекопитающие", 25)
    turtle_1 = Turtle('млекопитающие', 10, 'зеленая')
    print(turtle_1.return_species(), turtle_1.return_age())
