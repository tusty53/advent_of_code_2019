ADD = 1
MULTIPLY = 2
STOP = 99
TARGET = 19690720

if __name__ == "__main__":

    f = open("input.txt", "r")

    initial_numbers = [int(x) for x in f.readline().split(",")]

    for noun in range(100):
        for verb in range(100):
            pointer_position = 0
            input_numbers = initial_numbers.copy()
            input_numbers[1] = noun
            input_numbers[2] = verb

            while pointer_position < len(input_numbers):
                operator_value = input_numbers[pointer_position]
                if operator_value == STOP:
                    pointer_position = len(input_numbers)
                else:
                    number_1, number_2, result_position = input_numbers[input_numbers[pointer_position + 1]], \
                                                          input_numbers[input_numbers[
                                                              pointer_position + 2]], input_numbers[
                                                              pointer_position + 3]

                    if operator_value == ADD:
                        result = number_1 + number_2
                    if operator_value == MULTIPLY:
                        result = number_1 * number_2
                    input_numbers[result_position] = result

                    pointer_position += 4
            output = input_numbers[0]
            if output == TARGET:
                print(f"Target of {TARGET} has been reached. Noun value: {noun}, verb value: {verb}, result value(100 "
                      f"* noun + verb): {100 * noun + verb}")
                noun = 100
