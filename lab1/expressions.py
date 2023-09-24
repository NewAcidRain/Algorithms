from support_functuions import get_number, calculate_operation


operations = {
    "(": 0,
    "^": 1,
    "+": 2,
    "-": 2,
    "*": 3,
    "/": 3,
    "~": 4,
}


def calculate(expr: str):
    numbers_stack = []
    check_iteration = 0
    counter = 0
    for key, value in enumerate(expr):
        if value.isdigit():
            if check_iteration > key:
                continue
            else:
                check_iteration = 0
            number_fucntion = get_number(expr=expr, pos=key)
            number = number_fucntion['number']
            check_iteration += number_fucntion['iteration']
            numbers_stack.append(int(number))
        elif value in operations.keys():
            counter += 1
            if (value == "~"):
                last = numbers_stack.pop() if len(numbers_stack) > 0 else 0
                numbers_stack.append(calculate_operation(
                    operator='-', first=0, second=last))
                print(f"{counter}) {value}{last} = {numbers_stack[-1]}")
                continue
            second = numbers_stack.pop() if len(numbers_stack) > 0 else 0
            first = numbers_stack.pop() if len(numbers_stack) > 0 else 0
            numbers_stack.append(calculate_operation(
                operator=value, first=first, second=second))
            print(f"{counter}) {first} {value} {second} = {numbers_stack[-1]}")

    try:
        return numbers_stack.pop()
    except IndexError:
        raise Exception("Expression invalid")


def parse_expression(expr: str) -> str:
    output_string = ""
    check_iteration = 0
    stack = []
    expr = expr.replace('pow', '').replace(',', '^')
    if expr[0] != "(" or expr[-1] != ")":
        expr = "(" + expr + ")"
    if expr.count("(") != expr.count(")"):
        raise Exception("Number of brackets does not match")
    for key, value in enumerate(expr := expr.replace(" ", "")):
        if value.isalpha():
            raise Exception('Letters are not allowed')
        elif value.isdigit():
            if check_iteration >= key:
                continue
            else:
                check_iteration = 0
            numbers_function = get_number(expr=expr, pos=key)
            output_string += numbers_function['number'] + " "
            check_iteration += numbers_function['iteration']
        elif value == "(":
            stack.append(value)
        elif value == ")":
            while len(stack) > 0 and stack[-1] != "(":
                output_string += stack.pop()
            stack.pop()
        elif value in operations.keys():
            if value == '-' and ((key == 0 or key > 1) and (expr[key-1] in operations.keys())):
                value = "~"
            while len(stack) > 0 and operations[stack[-1]] >= operations[value]:
                output_string += stack.pop()
            stack.append(value)
        else:
            raise Exception("Value not allowed")

    for opertaion in stack:
        output_string += opertaion
    return output_string
