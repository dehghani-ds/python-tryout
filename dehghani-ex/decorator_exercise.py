import time

def timecalculator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"method {func.__name__} with parameter {args, kwargs} took {end - start} seconds")
    return wrapper

@timecalculator
def get_list_n(n):
    result_n = []
    for i in range(n):
        result_n.append(i)
    return result_n

get_list_n(1000)

get_list_n(12)

get_list_n(120000000)