'''version1 seed words result dig in'''
'''----for testing result and digging into raw dataset
input: a IR corpus, a expanding corpus(the candidate wordlist), a seed wordlist
output: a expanded seed wordlist
--------------'''
import math
import numpy as np
import timeit
start = timeit.default_timer()

file = open('D:/uw course/capstone/mypersonality/status_a_lemma.txt')#IR corpus

total=0
i=0
j=0
q=0
while 1:
#while total<=127679:
    line=file.readline()
    if not line:
        break
    #print(line)
    total+=1

    
    w1='mardou'
    w2='sweet memory'
    if line.find(w1)>-1:
        i+=1
    if line.find(w2)>-1:
        j+=1
    if (line.find(w1)>-1) & (line.find(w2)>-1):
        q+=1

file.close()
print(q)
print(i)
print(j)
print(total)
print(round(math.log(q/(i*j)*total),2))


elapsed = (timeit.default_timer() - start)
print(elapsed)
