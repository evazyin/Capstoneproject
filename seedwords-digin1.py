'''version2 seed words result dig in'''
'''----for extracting sentences containing the keywords
input: a IR corpus, a expanding corpus(the candidate wordlist), a seed wordlist
output: sentences (length>2) containing one keyword in one file
--------------'''
import math
import numpy as np
import timeit
start = timeit.default_timer()

file = open('D:/uw course/capstone/mypersonality/status_b_lemma.txt','r')#IR corpus
file1 = open('D:/uw course/capstone/mypersonality/wordlist-new1.txt','r')#keywords
keywordlist = file1.readline().split(',')
keywordcount = [0]*60
files = [open('D:/uw course/capstone/mypersonality/sentences1/%s.txt' %keywordlist[i], 'w') for i in range(60)]
total=0
i=0

while 1:
#while total<=127679:
    line=file.readline()
    if not line:
        break
    #print(line)
    total+=1

    for i in range(60):
        if line.find(keywordlist[i])>-1:
            files[i].write(line)
            keywordcount[i]+=1

file.close()
file1.close()
for f in files:
    f.close()
print(total)
print(keywordlist)
print(keywordcount)

elapsed = (timeit.default_timer() - start)
print(elapsed)
