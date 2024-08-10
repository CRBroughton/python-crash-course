def favouritePizzas():
    pizzas = ["Pepperoni", "Ham", "Cheese"]
    for pizza in pizzas:
        print(f"I like {pizza} pizza")


animals = ["Dog", "Cat", "Pig", "Bird", "Horse"]
def animalsAsPets(animals: list[str]):
    for animal in animals:
        print(f"A {animal} would make a great pet")


def getFirstThreeAnimals(animals: list[str]):
    print("The first three items in the list are:")
    for animal in animals[:3]:
        print(animal)

def getThreeAnimalsMiddle(animals: list[str]):
    print("The middle animals are:")
    for animal in animals[1:4]:
        print(animal)

def getLastThreeAnimals(animals: list[str]):
    print("The last three animals are:")
    for animal in animals[-3:]:
        print(animal)


def toTwenty():
    for value in range(1, 21):
        print(value)


def toOneMillion():
    for value in range(1, 1_000_001):
        print(value)


def sumOneMillion() -> int:
    values = [value for value in range(1, 1_000_001)]
    return sum(values)


def oddNumbers():
    values = [value for value in range(1, 20, 2)]
    return values


def listOfThrees():
    values = [value for value in range(3, 30, 3)]
    return values


def cubes():
    values = [value**3 for value in range(1, 11)]
    return values


def main():
    favouritePizzas()
    animalsAsPets(animals)
    toTwenty()
    toOneMillion()
    print(sumOneMillion())
    print(oddNumbers())
    print(listOfThrees())
    print(cubes())

    getFirstThreeAnimals(animals)
    getThreeAnimalsMiddle(animals)
    getLastThreeAnimals(animals)
main()
