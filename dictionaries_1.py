person = {
    'name': 'kidus',
    'age': 254,
    'email': 'kidus@mail.com'
}

# access email value
# method-1
# print(person['email'])
# method-2
# print(person.get('email'))

# get keys
# print(person.keys())
# get values
# print(person.values())
# get items
# print(person.items())

# update the age to 25
# person.update({'age': 25})

# update person by adding city of the person
# person.update({'city': 'boston'})

# delete item with specified key name
# del person['age']
# person.pop('age')

# delete last inserted item
# person.popitem()

# delete person dictionary
# del person
# clear person dictionary
# person.clear()

# print person keys one by one
# for x in person.keys():
#     print(x)
# # print peson values one by one
# for y in person.values():
#     print(y)

# print items in person
# for x, y in person.items():
#     print(x,y)

# # print(person)