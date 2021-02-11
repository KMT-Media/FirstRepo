# functions

# emoji converter

def emoji_converter(message):
    word = message.split()
    emoji_match = {
        'happy': '🙂', 
        'sad': '😟' 
    }
    output = ''
    for wds in word:
        output += emoji_match.get(wds, wds) + ' '
    return output

# message = input('>')
# result = emoji_converter(message)
# print(result)

# write a proram which can compute factorial of given numebrs
# def fact(x):
#     if x == 0:
#         return 1
#     return x * fact(x-1)
# x = 5
# print(fact(x))

# Define a class which has at least two methods: 
# getString: to get a string from console input printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

class InputOutput:
    def __init__(self):
        self.s = ''
    
    def prompt(self):
        self.s = input()

    def capital(self):
        print(self.s.upper())

# test = InputOutput()
# test.prompt()
# test.capital()

