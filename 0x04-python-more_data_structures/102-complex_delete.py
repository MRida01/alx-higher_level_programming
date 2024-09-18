#!/usr/bin/python3
def complex_delete(my_dict, value):
    todelete = []
    for key in my_dict:
        if my_dict[key] == value:
            todelete.append(key)
    for key in todelete:
        del my_dict[key]
    return my_dict
