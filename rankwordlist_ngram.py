import timeit
from functools import reduce

start = timeit.default_timer()
file = open('D:/uw course/capstone/mypersonality/wordlist_3gram_freqover3_IRBack_13w_thre0.001.txt')#expanded wordlist
file1 = open('D:/uw course/capstone/mypersonality/stopwords.txt','r')
file2 = open('D:/uw course/capstone/mypersonality/wordlist_lemma.txt','r')
line = file.readline()
linestr = reduce(lambda line,c: line.replace(c, ''), '[]', line)
wordlist = linestr.split(',')
stopwords=file1.readline().split(",")
keywords=file2.readline().split(",")
expword=[[0 for column in range(3)] for row in range(int(len(wordlist)/3))]
q=0
for i in range(int(len(wordlist)/3)):
    elim = 0;
    for w in stopwords:
        if w in wordlist[i*3]:
            elim+=1
    for w1 in keywords:
        if w1 in wordlist[i*3]:
            elim+=1
    print(elim)
    if elim==0:
        expword[q][0]=wordlist[i*3]
        expword[q][1]=float(wordlist[i*3+1])
        expword[q][2]=wordlist[i*3+2]
        q+=1
print(q)
expword = sorted(expword, key=lambda x: x[1], reverse=True)
if q>20:
    for j in range(20):
        print(str(j+1)+' '+str(expword[j][0])+' '+str(expword[j][1])+' '+str(expword[j][2]))    
else:
    for j in range(q):
        print(str(j+1)+' '+str(expword[j][0])+' '+str(expword[j][1])+' '+str(expword[j][2]))

file.close()
file1.close()
file2.close()
