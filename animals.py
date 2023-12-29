class Animal:
    def __init__(self, name):
        self.name = name
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def list_commands(self):
        return ', '.join(self.commands)


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def bark(self):
        return "Woof!" # Так поинтереснее звучит :)


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def meow(self):
        return "Meow!" # Ну раз собака на англ. то и кошка пусть также будет :)


class AnimalRegistry:
    def __init__(self):
        self.animals = {}

    def add_animal(self, animal):
        self.animals[animal.name] = animal

    def get_animal(self, name):
        return self.animals.get(name, None)

def menu():
    registry = AnimalRegistry()

    while True:
        print("\n\n\n1. Добавить собаку")
        print("2. Добавить кошку")
        print("3. Добавить комманду для животного")
        print("4. Посмотреть список комманд")
        print("5. Попросить собаку полаять :) ")
        print("6. Попросить кошку мяукнуть :) ")
        print("7. Выйти")

        choice = input("Что хотите сделать? : ")

        if choice == "1":
            print("======================= \n")
            name = input("Как зовут собаку? : ")
            breed = input("Укажите породу: ")
            dog = Dog(name, breed)
            registry.add_animal(dog)

        elif choice == "2":
            print("======================= \n")
            name = input("Укажите имя кота: ")
            color = input("ВВедите цвет шёрстки: ")
            cat = Cat(name, color)
            registry.add_animal(cat)

        elif choice == "3":
            print("======================= \n")
            name = input("Кого хотите обучить? введите имя питомца: ")
            command = input("Введите команду: ")

            animal = registry.get_animal(name)
            if animal:
                animal.add_command(command)
            else:
                print(f"Питомца: {name} нет в нашем питомнике, Вы можете добавить его.")

        elif choice == "4":
            print("======================= \n")
            name = input("Позовите питомца к себе (введите имя): ")

            animal = registry.get_animal(name)
            if animal:
                print(f"{name} может выполнить одну из команд: {animal.list_commands()}")
            else:
                print(f"Питомца: {name} нет в нашем питомнике, Вы можете добавить его.")

        elif choice == "5":
            print("======================= \n")
            name = input("Окликните собачку: ")

            animal = registry.get_animal(name)
            if isinstance(animal, Dog):
                print(f"\n\n\n {name} радостно отзывается: {animal.bark()}")
            else:
                print(f"У нас нет {name} в питомнике или {name} не собака.")

        elif choice == "6":
            print("======================= \n")
            name = input("Окликните котейку: ")

            animal = registry.get_animal(name)
            if isinstance(animal, Cat):
                print(f"\n\n\n {name} радостно отзывается: {animal.meow()}")
            else:
                print(f"У нас нет {name} в питомнике или {name} не котейка.")

        elif choice == "7":
            break

        else:
            print("Вы выбрали неверный пункт меню, сделайте правильный выбор!.")


if __name__ == "__main__":
    menu()
