def do_addition(a,b):
    return a+b

def do_subtraction(a,b):
    return a-b

def do_multiplication(a,b):
    return a*b

def do_divison(a,b):
    try:
        return a/b
    except ZeroDivisionError as e:
        print("divison by zero is not possible")


