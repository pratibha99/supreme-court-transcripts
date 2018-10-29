import regex as re
import numpy
import os

def unique(texts):
    list(set(texts))

#return a set of nonunique bill mentioned in the speech.
def bill(texts):
    no_num = re.sub('\d+','',texts)
    no_n = re.sub('\n','',no_num)
    evenly_spaced = re.sub('\s+',' ',no_n)
    b= re.findall("[A-Z][a-z]+\s[A-Z][a-z]+\sAct", evenly_spaced)
    return b
#return a set of unique bill mentioned in the speech.
def unibill(texts):
    return unique(bill(texts))
#return the name and times it appears.
def count(texts):
    bills = bill(texts)
    ret = []
    for i in range(0,len(bills)):
        count = bills.count(bills[i])
        ret.append (str(bills[i]) + " " + ":" + ' '+str(count))
    return unique(ret)
