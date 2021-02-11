import math

# ask user to input weight(in pounds), converted to kg and print on the terminal
# wgh_lbs = input('weight (lbs): ')
# wgh_kg = int(wgh_lbs) * 0.45
# print('weight (kg): ', wgh_kg)

# ask user to input weight(in pound or kg), converted to desired out put
# weight = int(input('Weight: '))
# unit = input('(L) lbs, (k) kg: ')
# if unit.lower() == 'k':
#     convert = weight / 0.45
#     print('your weight in lbs:', convert)
# elif unit.lower() == 'l':
#     convert = weight * 0.45
#     print('your weight in kg:', convert)
# else:
#     print('wrong input')

# build a car game 
# prompt = ''
# car_started = False
# car_stopped = False
# while True:
#     prompt = input('>').lower()

#     if prompt == 'help':
#         print('start - to start the car\nstop - to stop the car\nquit - to exit')
#     elif prompt == 'start':
#         if car_started:
#             print('car already started')
#         else:
#             car_started = True
#             print('car  started.. ready to go')
        
#     elif prompt == 'stop':
#         if car_stopped:
#             print('car already stopped...')
#         else:
#             car_stopped = True
#             print('car stopped')

#     elif prompt == 'quit':
#         quit()
#     else:
#         print("I don't understand that")

# using the following list convert the list to shape
numbers = [5, 2, 5, 2, 2]
# for x in numbers:
#     for y in range(x, x+1):
#         print('x' * y)

# method-2
# for x in numbers:
#     print('X' * x)

# method-3
# for x in numbers:
#     output = ''
#     for y in range(x):
#         output += 'x'
#     print(output)

# write a program to find the largest numbers in a list
number = [3, 6, 2, 4, 8, 10]

# method-1
# print(max(number))

# method-2
# largest = number[0]
# for num in number:
#     if num > largest:
#         largest = num
# print(largest)

# write a program that removes duplicates in a list
phone_num = [76, 38, 93, 28, 38, 93, 28]
# method-1
# for num in phone_num:
#     if phone_num.count(num) > 1:
#         phone_num.remove(num)
# print(phone_num)

# method-2
# unique = []
# for num in phone_num:
#     if num not in unique:
#         unique.append(num)
# print(unique)

# write a program that accepts comma separated sequences of words as input
# and prints words in comma separated sequences after sorting them alphabeticaly
items = [x for x in input().split(',')]
items.sort()
print(','.join(items))

# write a number dictionary
# phone = input('Phone: ')

# di = {
#     '1': 'one',
#     '2': 'two',
#     '3': 'three',
#     '4': 'four',
# }

# match = ''
# for ch in phone:
#     match += di.get(ch, '!') + ' '
# print(match)

# With a given integral number n, write a program to generate a dictionary that contains (i, i*i)
# num = int(input('>'))
# di = dict()
# for value in range(1, num+1):
#     di[value] = value **2
# print(di)

# find floor of a value
# floor = math.floor(3.4) # 3

# find ceil of a value
# ceil = math.ceil(3.4) # 4

# print(floor, ceil)