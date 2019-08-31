def pattern_1(loop_count):
    for i in range(1, loop_count + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


def pattern_2(loop_count):
    for i in range(1, loop_count + 1):
        value = "Fizz" if is_fizz(i) else ""
        value += "Buzz" if is_buzz(i) else ""
        value += str(i) if not(is_fizz(i) or is_buzz(i)) else ""
        print(value)


def is_fizz(number):
    return number % 3 == 0


def is_buzz(number):
    return number % 5 == 0


if __name__ == "__main__":
    print("start - pattern_1")
    pattern_1(100)

    print("start - pattern_2")
    pattern_2(100)
