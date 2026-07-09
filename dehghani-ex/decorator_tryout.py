def time_decorator(func):
    def wrapper(*args, **kwargs):
        print("on decorator with args[{}] and keyword[{}]".format(args, kwargs))
        res = func(args[0])
        print(f"on decorator after call return={res}")
    return wrapper

@time_decorator
def say_hello(name):
    print('Hello World! {} - type[{}]'.format(name, type(name)))
    return 2

@time_decorator
def say_goodbye(name):
    print('Goodby! {}'.format(name))

say_hello('reza')
say_goodbye('gholi')