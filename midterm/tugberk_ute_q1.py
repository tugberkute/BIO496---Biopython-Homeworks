def operand_check(operand: str):
    """
    :param operand: operand as string
    :return: True if operand is valid, false if it is not
    """
    if operand not in ["+", "-", "*", "/"]:
        return False
    else:
        return True


def number_input_check(nums: str):
    """
    :param nums: user input as string
    :return: True and number 1 and number 2 if the user entered space delimited two numbers, False and error message if not
    """
    try:
        num1, num2 = map(int, nums.split(" "))
    except:
        return False, "Your input is wrong. Please enter two space delimited numbers!\n", None, None

    return True, None, int(num1), int(num2)


def operation(num1: int, num2: int, op: str):
    """
    Takes valid numbers and operand and calculates the result
    :param num1: integer
    :param num2: integer
    :param op: operand
    :return: result of operation
    """
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "/":
        return num1 / num2
    elif op == "*":
        return num1 * num2


def main():
    while True:
        operand = input("Please give me an operand: ")
        if not operand_check(operand):
            continue
        else:
            while True:
                numbers = input("Please enter two space delimited numbers: ")
                valid, error, num1, num2 = number_input_check(numbers)
                if not valid:
                    print(error)
                    continue
                else:
                    print(f"Your result is: {operation(num1, num2, operand)}")
                    exit()


main()
