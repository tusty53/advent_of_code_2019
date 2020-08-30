import math


def calculate_fuel(weight):
    return math.floor(weight / 3) - 2


if __name__ == "__main__":

    f = open("input.txt", "r")
    total_fuel = 0
    new_fuel = 0

    for line in f.readlines():
        new_fuel = calculate_fuel(int(line))
        while new_fuel > 0:
            total_fuel += new_fuel
            new_fuel = calculate_fuel(new_fuel)

    print(total_fuel)
