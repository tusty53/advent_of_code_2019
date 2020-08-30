MIN_VAL = 256310
MAX_VAL = 732736


def check_complicated_pairs(x):
    num_string = str(x)
    previous_digit = 0
    same_digit_count = 0
    for i in range(6):
        current_digit = num_string[i]
        if current_digit == previous_digit:
            same_digit_count += 1
        else:
            previous_digit = current_digit
            if same_digit_count == 2:
                return True
            same_digit_count = 1
    if same_digit_count == 2:
        return True
    return False


def check_not_decreasing(x):
    num_string = str(x)
    for i in range(5):
        if int(num_string[i]) > int(num_string[i + 1]):
            return False
    return True


if __name__ == "__main__":
    number_of_good_passwords = 0
    for x in range(MIN_VAL, MAX_VAL):
        if check_not_decreasing(x) and check_complicated_pairs(x):
            print(x)
            number_of_good_passwords += 1
    print(number_of_good_passwords)
