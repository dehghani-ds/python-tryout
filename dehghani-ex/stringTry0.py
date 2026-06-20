name = "Ali ramezanpour amir dehi"
age = 25
print(name[::-2], age)
print("""jadi
mirmirani
""")
print(name.islower())

# string format
print("my name is {1} and my age is {0}".format(name, age))
print("my name is {name} and my age is {age}".format( age=age, name =name))

print(f"my name is {name} and my age is {age}") # this is a format string