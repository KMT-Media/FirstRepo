# file handling operation order

# open file
file_object = open('file/clown.txt', 'r')
# perform operation(read or write)
file_object.read()
# close
file_object.close()

# same as above
with open('file/clown.txt', 'r') as file_object:
    file_object.read() # read till the end of line # 'first line/nsecondline/n'
    file_object.read() # further reading returns empty string

with open('file/clown.txt', 'r') as f:
    for line in f:
        # using for loop also return a newline(empty string)
        print(line)

    # chencing modes
    f.readable() ## TRUE
    f.writable() ## FALSE
    f.seekable() ## TRUE