# text files are thought of us a sequence of lines
# open() - returns a file handle - makes python possible so that u can read the file
# handle steps - open() - read or write - close()
# mode is optional - 'r' - read or 'w' - write or 'a' - append or 'r+' - read and write 

xfile = open('mbox-short.txt') # file handle object
# xfile = open('mbox-short.txt', 'rt') 
# same as above, 'r' - for read and 't' - for text
# print(xfile.read()) # returns the whole txt # string class

 
# read the 1st and 2nd line in your file
# print(xfile.readline())
# print(xfile.readline())

# read all lines in your file
# method-1 # by making the an list
# print(xfile.readlines())
# method-2
# for line in xfile:
#     print(line)

# read the 37 line in your file
# print(xfile.readlines()[37])

# count lines in a file
# count = 0
# for line in xfile:
#     count += 1
# print('line count:',count)

# get the length of a file & print the first 20 chars
# read_file = xfile.read()
# print(len(read_file))
# print(read_file[:20])

# print lines that starts with 'From'
# for line in xfile: 
#     line = line.rstrip() 
#     if line.startswith('From:'):
#         print(line)
# method-2
# for line in xfile:
#     line = line.rstrip()
#     if not line.startswith('From:'):
#         continue
#     print(line)

# using "in" print lines start with '@uct.ac.za'
# for line in xfile:
#     line = line.rstrip()
#     if not '@uct.ac.za' in line:
#         continue
#     print(line)

# prompt file for file name & count how many lines are there that starts with "subject"
# file_name = input('Enter file: ')
# try:
#     xfile = open(file_name)
# except:
#     print('file cannot be opend ', file_name)
#     exit()
# count = 0
# for line in xfile:
#     if not 'Subject' in line:
#         continue
#     count += 1
# print('There were', count, 'subject lines in', file_name)

xfile.close()


# add txt file in clown-txt
# file = open('clown.txt', 'a')
# file.write('appended txt')
# file.close()

# file = open('clown.txt', 'r')
# print(file.read())


# create a file called 'kidus.txt
# kidus = open('kidus.txt', 'x')

# extract one line that starts with From:
# and extract email of that line
# extract characters after @