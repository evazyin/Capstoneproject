import timeit
from functools import reduce

start = timeit.default_timer()
file = open('D:/uw course/capstone/mypersonality/wordlist_3gram_freqover10_IRBack_21w_thre0.05.txt')#expanded wordlist
line = file.readline()
linestr = reduce(lambda line,c: line.replace(c, ''), '[]', line)
wordlist = linestr.split(',')
expword=[[0 for column in range(3)] for row in range(int(len(wordlist)/3))]
for i in range(int(len(wordlist)/3)):
    expword[i][0]=wordlist[i*3]
    expword[i][1]=float(wordlist[i*3+1])
    expword[i][2]=wordlist[i*3+2]
print(i+1)
expword = sorted(expword, key=lambda x: x[1], reverse=True)
if len(wordlist)/3>20:
    for j in range(20):
        print(str(j+1)+' '+str(expword[j][0])+' '+str(expword[j][1])+' '+str(expword[j][2]))    
else:
    for j in range(int(len(wordlist)/3)):
        print(str(j+1)+' '+str(expword[j][0])+' '+str(expword[j][1])+' '+str(expword[j][2]))

