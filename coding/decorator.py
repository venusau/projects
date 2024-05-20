def add(func):
    def wrapper(a, b):
        s = a + b
        print("Sum of the two numbers:", s)
        return func(a, b)
    return wrapper

@add
def sub(a, b):
    print("Difference of the two numbers:", a - b)

sub(10, 20)
