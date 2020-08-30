ADD = 1
MULTIPLY = 2
STOP = 99

if __name__ == "__main__":

    f = open("input.txt", "r")
    input_numbers = [int(x) for x in f.readline().split(",")]

    print(input_numbers)
    pointer_position = 0

    input_numbers[1] = 12
    input_numbers[2] = 2

    while pointer_position < len(input_numbers):
        operator_value = input_numbers[pointer_position]
        if operator_value == STOP:
            pointer_position = len(input_numbers)
        else:
            number_1, number_2, result_position = input_numbers[input_numbers[pointer_position + 1]], input_numbers[input_numbers[
                pointer_position + 2]], input_numbers[pointer_position + 3]

            if operator_value == ADD:
                result = number_1 + number_2
            if operator_value == MULTIPLY:
                result = number_1 * number_2
            input_numbers[result_position] = result

            pointer_position += 4
    print(input_numbers)
