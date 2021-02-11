# propt the user to enter a file
# find the common word in that file


xfile = input('Enter file:')
if len(xfile) < 1: xfile = 'clown.txt'
handle = open(xfile)

# dict
di = dict()
for line in handle:
    line = line.rstrip()
    wds = line.split()
    for w in wds:
        # idiom: retrieve/create/ update counter
        # method-1
        di[w] = di.get(w, 0) + 1

        # method-2
        # oldcount = di.get(w, 0)
        # print('**',w, oldcount)
        # newcount = oldcount + 1
        # di[w] = newcount
        # print('**',w,newcount)

# print(di)

# find the mosto common word
largest = 0
word = None
for k,v in di.items():
    if v > largest:
        largest = v
        word = k
print(word,largest)



