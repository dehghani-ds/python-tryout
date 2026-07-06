def sum_numbers(*args):
    sums = 0
    for arg in args:
        sums += arg
    return sums

print(sum_numbers(1, 2, 3, 5, 7, 9))