#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = 0
    b = 0
    c = 0
    d = 0
    if len(tuple_a) > 1:
        a, b = tuple_a[0], tuple_a[1]
    elif len(tuple_a) == 1:
        a = tuple_a[0]
    if len(tuple_b) > 1:
        c, d = tuple_b[0], tuple_b[1]
    elif len(tuple_b) == 1:
        c = tuple_b[0]
    result = (a + c, b + d)
    return result
