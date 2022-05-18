import random

with open('../files/dataname.txt', 'r', encoding='utf8') as fp:
    name_read = fp.read()
name_list = name_read.split('\n')
numbers = random.sample(range(0, len(name_list)), len(name_list))
print(numbers)