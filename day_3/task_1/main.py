import math

WIND_ROSE = \
    {
        "U": (0, 1),
        "D": (0, -1),
        "R": (1, 0),
        "L": (-1, 0),
    }


def create_wire_path(wire):
    wire_path = set()
    current_x, current_y = 0, 0
    for instruction in wire:
        direction = instruction[0]
        distance = int(instruction[1:])
        # print(f"Direction: {direction}, distance: {distance}")

        for i in range(distance):
            current_x += WIND_ROSE[direction][0]
            current_y += WIND_ROSE[direction][1]
            wire_path.add((current_x, current_y))

    return wire_path


if __name__ == "__main__":
    f = open("input.txt", "r")
    wire_1 = f.readline().split(",")
    wire_2 = f.readline().split(",")

    wire_1_path = create_wire_path(wire_1)
    wire_2_path = create_wire_path(wire_2)

    min_dist = math.inf
    closest_intersection = None

    for point in wire_1_path:
        if wire_2_path.__contains__(point) and abs(point[0]) + abs(point[1]) < min_dist:
            closest_intersection = point
            min_dist = abs(point[0]) + abs(point[1])

    print(f"Closest intersection = {closest_intersection}, min distance = {min_dist}")