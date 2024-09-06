def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator  #say_hello=my_decorator(say_hello)
def say_hello():
    print("Hello!")




say_hello()