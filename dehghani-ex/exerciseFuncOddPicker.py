def pick_evens(*args):
    odd = []
    for arg in args:
        if arg % 2 == 0:
            odd.append(arg)
    return odd

def skyline(*args):
    return 0 if len(args) == 0 else max(args)



print(pick_evens(2,3,24,23,5,245,63467,35,7,357))
print(skyline(2,3,24,23,5,245,63467,35,7,357))
print(skyline())