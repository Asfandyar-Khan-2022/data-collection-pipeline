def my_decorator(func):
    def wrapper(*args,**kwargs):
        test = func(*args,**kwargs)
        with open('out.txt', 'w') as f:
            print(test, file=f)  # Python 3.
        return test

    return wrapper
    

@my_decorator
def say_hello(name):
    return f'Hello, {name}!'

say_hello('Asfandyar')