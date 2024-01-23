#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            quotient = my_list_1[i] / my_list_2[i]
        except (ZeroDivisionError, TypeError, IndexError) as e:
            if isinstance(e, ZeroDivisionError):
                print("division by 0")
            elif isinstance(e, TypeError):
                print("wrong type")
            elif isinstance(e, IndexError):
                print("out of range")
            quotient = 0
        finally:
            result.append(quotient)
    return result
