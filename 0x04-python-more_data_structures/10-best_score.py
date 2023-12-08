#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        first = list(a_dictionary)[0]
        best = first
        for i in a_dictionary:
            if a_dictionary[i] > a_dictionary[best]:
                best = i
        return best
    return None
