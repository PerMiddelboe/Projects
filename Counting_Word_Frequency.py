fname = input('Enter File: ')
if len(fname) < 1 : fname = 'mbox-short.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    # Print(lin)
    wds = lin.split()
    # Print(wds)
    for w in wds:
        # if the key is not there the count is zero
        # oldcount = di.get(w,0)
        # print(w,'old', oldcount)
        # newcount = oldcount + 1
        # di[w] = newcount

        # idiom: retieve/create/update counter
        di[w] = di.get(w,0) + 1
        # print(w, 'new', di[w]) 

# print(di)               

# now we want to find the most common word
largest = -1
theword = None
for k,v in di.items() :
    # print(k,v)
    if v > largest :
        largest = v
        theword = k #capture/remember the key that was largest 

print('The most common word is:', theword, "It is mentioned ", largest , ' times.' )        