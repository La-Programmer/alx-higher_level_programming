#!/usr/bin/python3
"""python3 -c 'print(__import__("3-say_my_name.py").__doc__)'
"""


def say_my_name(first_name, last_name=""):
    """python3 -c 'print(__import__("3-say_my_name.py").say_my_name.__doc__)'
    """
    err_msg1 = "first_name must be a string"
    err_msg2 = "last_name must be a string"
    err_msg3 = "first_name cannot be empty"
    if not isinstance(first_name, str):
        raise TypeError(err_msg1)

    if not isinstance(last_name, str):
        raise TypeError(err_msg2)

    if first_name == "":
        raise ValueError(err_msg3)

    if last_name == "":
        print("My name is {}".format(first_name))
    else:
        print("My name is {} {}".format(first_name, last_name))
