import math

WIND_ROSE = \
    {
        "U": (0, 1),
        "D": (0, -1),
        "R": (1, 0),
        "L": (-1, 0),
    }


def create_wire_path(wire):
    wire_path = dict()
    current_x, current_y = 0, 0
    steps = 0
    for instruction in wire:
        direction = instruction[0]
        distance = int(instruction[1:])

        for i in range(distance):
            current_x += WIND_ROSE[direction][0]
            current_y += WIND_ROSE[direction][1]
            steps += 1
            wire_path[current_x, current_y] = steps

    return wire_path


if __name__ == "__main__":
    f = open("input.txt", "r")
    wire_1 = f.readline().split(",")
    wire_2 = f.readline().split(",")

    wire_1_path = create_wire_path(wire_1)
    wire_2_path = create_wire_path(wire_2)

    min_dist = math.inf
    closest_intersection = None

    for point in wire_1_path.keys():
        if wire_2_path.keys().__contains__(point) and wire_1_path[point] + wire_2_path[point] < min_dist:
            closest_intersection = point
            min_dist = wire_1_path[point] + wire_2_path[point]

    print(f"Closest intersection = {closest_intersection}, min distance = {min_dist}")