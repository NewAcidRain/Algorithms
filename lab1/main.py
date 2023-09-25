from expressions import *


if __name__ == "__main__":
    while (True):
        a = input()
        postfix = parse_expression(a)
        print(f"Postfix entry : {postfix}")
        print(calculate(postfix))
