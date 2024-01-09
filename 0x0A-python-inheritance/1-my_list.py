#!/usr/bin/python3
"""python3 -c 'print(__import__("1-my_list.py").__doc__)'
"""


class MyList(list):
    """python3 -c 'print(__import__("1-my_list.py").MyList.__doc__)'
    """
    

    def print_sorted(self):
        print(sorted(self))
