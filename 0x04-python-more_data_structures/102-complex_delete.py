#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    holder = {x: a_dictionary[x] for x in a_dictionary}
    for i in holder:
        if holder[i] == value:
            del a_dictionary[i]
    return a_dictionary
