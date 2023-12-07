#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    holder = set(my_list)
    for i in holder:
        result += i
    return result
