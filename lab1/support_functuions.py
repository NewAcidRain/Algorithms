

from typing import Union


def get_number(expr: str, pos: int) -> str:
    number = ""
    while pos < len(expr):
        if expr[pos].isdigit():
            number += expr[pos]
            pos += 1
        else:
            break

    return {"number": number, "iteration": pos}


def calculate_operation(operator: str, first: Union[int, float], second: Union[int, float]) -> Union[int, Exception]:
    operation_result = 0
    match operator:
        case "+":
            try:
                operation_result = first + second
            except:
                raise Exception("invalid parametrs")
        case "-":
            operation_result = first - second
        case "*":
            operation_result = first * second
        case "/":
            try:
                operation_result = first / second
            except ZeroDivisionError:
                raise Exception("Division on 0 not allowed")
        case "^":
            operation_result = first ** second
        case _:
            raise Exception("Operation not found")
    return operation_result
