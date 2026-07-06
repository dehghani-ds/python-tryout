def pick_evens(*args):
    odd = []
    for arg in args:
        if arg % 2 == 0:
            odd.append(arg)
    return odd

print(pick_evens(2,3,24,23,5,245,63467,35,7,357))