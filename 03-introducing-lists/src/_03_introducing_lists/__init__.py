from typing import List

names = ["Craig", "Jake", "Chris", "Kal", "Alberto"]


def printNames(names: List[str]):
    for name in names:
        print(name)


def greetings(names: List[str]):
    for name in names:
        print(f"Hello {name}")


motorCycles = ["honda", "yamaha", "suzuki"]


def updateMotorcycles(motorcycles: List[str], newValue: str) -> List[str]:
    motorcycles.append(newValue)
    return motorcycles


def insertMotorcycle(motorcycle: str, position: int) -> List[str]:
    motorCycles.insert(position, motorcycle)
    return motorCycles


def removeMotorcycle(motorcycles: List[str], position: int) -> List[str]:
    del motorcycles[position]
    return motorcycles


locations = ["Greece", "Italy", "Japan", "New Zealand", "Iceland"]


def locationFunction():
    print(locations)
    print(sorted(locations))
    print(locations)
    locations.sort(reverse=True)
    print(locations)
    locations.reverse()
    print(locations)
    locations.sort()
    print(locations)


def main():
    printNames(names)
    greetings(names)

    print(updateMotorcycles(motorCycles, "ducati"))
    print(insertMotorcycle("new-one", 0))
    print(removeMotorcycle(motorCycles, 2))

    locationFunction()


main()
