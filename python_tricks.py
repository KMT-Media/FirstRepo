# ternary operator
# 1
Condition = True
if Condition:
    x = 5
else:
    x = 2

# same as above
if Condition: x = 5
else: x = 2

# same as above
x = 5 if Condition else 2

print(x)

# 2 underscore dosen't affect numbers
num1 = 10_000_000_000
num2 = 200_000
sum = num1 + num2
# separate by comma
print(f'{sum:,}')

# get only integer no. of any division
div =  5 // 2
print(div) # 2

# file handling - avoid using close()
# conext manager
with open('clown.txt', 'r') as f:
    file_content = f.read()
words = file_content.split()
word_count = len(words)
print(word_count)

# get the index and list
names = ['kidus', 'hanna', 'abel']
for index, name in enumerate(names, start=1):
    print(index, name)
# loop through two lists at one function
heros = ['Peter parker', 'Clark kent', 'Wade willson', 'Bruce Wayne']
alias = ['Spider man', 'Super man', 'Dead pool', 'Bat man']
universe = ['Marvel', 'DC', 'Marvel', 'DC']
# get index and match heros to alias
# method-1 
count = 0
for hero in heros:
    name = alias[count]
    print(count, hero, name)
    count += 1
# methon-2

for index, hero in enumerate(heros):
    name = alias[index]
    print(index, hero, name)
# by unpacking method match heros, alias and universe
# packing - creating tuple class

for value in zip(heros, alias, universe):
    print(value)
# unpacking - creating string class

for hero, ali, uni in zip(heros, alias, universe):
    print(hero, ali, uni)

# unpacking explaind
# normal
items = (5, 8)
# unpacking
a, *b = (5, 8, 23)
print(a)
print(b) # [8, 23]


# dynamicly add attribute to class
class Person:
    pass
# instantiate
person = Person()
# attribute and value
# person.first = 'kidus'
# print(person.first)

# same as above
first_key = 'first'
first_val = 'kidus'
# set attribute
# setattr(person, first_key, first_val)
# print(person.first)

# get attr
# first = getattr(person, first_key)
# print(first)

# person dictionary
person_info = {'first': 'kidaa', 'last': 'tadaa'}
# loop through each key and value
for key, value in person_info.items():
    # set attribute
    setattr(person, key, value)
# print(person.first)
# print(person.last)
for key in person_info.keys():
    print(getattr(person, key))