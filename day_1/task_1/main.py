import math


def calculate_fuel(weight):
    return math.floor(weight / 3) - 2


if __name__ == "__main__":

    f = open("input.txt", "r")
    total_fuel = 0

    for line in f.readlines():
        total_fuel += calculate_fuel(int(line))

    print(total_fuel)
