#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    operators = ['+', '-', '*', '/']
    index = 10
    a = argv[1]
    b = argv[3]
    op = argv[2]
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    for i in range(len(operators)):
        if op == operators[i]:
            index = (index - 10) + i
            break
        else:
            continue
    if index == 10:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    elif index == 0:
        print('{} {} {} = {}'.format(a, op, b, add(int(a), int(b))))
        exit(0)
    elif index == 1:
        print('{} {} {} = {}'.format(a, op, b, sub(int(a), int(b))))
        exit(0)
    elif index == 2:
        print('{} {} {} = {}'.format(a, op, b, mul(int(a), int(b))))
        exit(0)
    else:
        print('{} {} {} = {}'.format(a, op, b, div(int(a), int(b))))
        exit(0)
