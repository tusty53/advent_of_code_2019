MIN_VAL = 256310
MAX_VAL = 732736


def check_pairs(x):
    num_string = str(x)
    for i in range(5):
        if num_string[i] == num_string[i+1]:
            return True
    return False


def check_not_decreasing(x):
    num_string = str(x)
    for i in range(5):
        if int(num_string[i]) > int(num_string[i+1]):
            return False
    return True


if __name__ == "__main__":
    number_of_good_passwords = 0
    for x in range(MIN_VAL, MAX_VAL):
        if check_pairs(x) and check_not_decreasing(x):
            print(x)
            number_of_good_passwords += 1
    print(number_of_good_passwords)
