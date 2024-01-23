def safe_print_division(a, b):
    result = None
    try:
        result = a / b
        print("{:d} / {:d} = {}".format(a, b, result))
    except ZeroDivisionError:
        print("{:d} / {:d} = {}".format(a, b, result))
    finally:
        print("Inside result: {}".format(result))
    return result
