def favouritePizzas():
    pizzas = ["Pepperoni", "Ham", "Cheese"]
    for pizza in pizzas:
        print(f"I like {pizza} pizza")


def animalsAsPets():
    animals = ["Dog", "Cat", "Pig"]
    for animal in animals:
        print(f"A {animal} would make a great pet")


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
    animalsAsPets()
    toTwenty()
    toOneMillion()
    print(sumOneMillion())
    print(oddNumbers())
    print(listOfThrees())
    print(cubes())


main()
