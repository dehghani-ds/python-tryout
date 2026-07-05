i = int(input())

type_input = {3: 'جادویی', 5: 'نفرین شده', 15: 'افسانه ای'}

if i % 3 == 0 and i % 5 == 0:
    print(type_input[15])
elif i % 3 == 0 and i % 5 != 0:
    print(type_input[3])
elif i % 3 != 0 and i % 5 == 0:
    print(type_input[5])
else:
    print('معمولی')