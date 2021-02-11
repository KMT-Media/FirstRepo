# we can put a tuple on the left-hand side of an assignment statment
# we can omit the parenthesis
# (a,b) = (99,'name') - print(a) - 99 - print(b) - 'name'

# propt the user to enter a file
# find the top 10 common words in that file

xfile = input('Enter file:')
if len(xfile) < 1: xfile = 'clown.txt'
handle = open(xfile)

di = dict()
for line in handle:
    line = line.rstrip()
    wds = line.split()
    for w in wds:
        di[w] = di.get(w, 0) + 1

# sort by key    
# x = sorted(di.items())
# print(x[:5])

# sort by value 
lis = list()
for k,v in di.items():
    newtup = (v,k)
    lis.append(newtup)
lis = sorted(lis, reverse=True)
for k,v in lis[:5]:
    print(v,k)