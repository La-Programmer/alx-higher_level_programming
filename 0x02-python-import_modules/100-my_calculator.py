#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    operators = ['+', '-', '*', '/']
    index = 10
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    for i in range(len(operators)):
        if argv[2] == operators[i]:
            index = (index - 10) + i
            break
        else:
            continue
    if index == 10:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    elif index == 0:
        print('{} {} {} = {}'.format(argv[1], argv[2], argv[3], add(int(argv[1]), int(argv[3]))))
        exit(0)
    elif index == 1:
        print('{} {} {} = {}'.format(argv[1], argv[2], argv[3], sub(int(argv[1]), int(argv[3]))))
        exit(0)
    elif index == 2:
        print('{} {} {} = {}'.format(argv[1], argv[2], argv[3], mul(int(argv[1]), int(argv[3]))))
        exit(0)
    else:
        print('{} {} {} = {}'.format(argv[1], argv[2], argv[3], div(int(argv[1]), int(argv[3]))))
        exit(0)
