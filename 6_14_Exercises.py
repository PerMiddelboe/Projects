from multiprocessing.sharedctypes import Value

str = 'X-DSPAM-Confidence:0.8475'

ppp = str.find(':')
# print(ppp)
pppp = str[ppp+1:]
# print(pppp)
rrr = float(pppp)
print(rrr)