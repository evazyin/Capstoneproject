'''version1 seed words algorithm'''
'''------------
input: a IR corpus, a expanding corpus(the candidate wordlist), a seed wordlist
output: a expanded seed wordlist
--------------'''
import math

file = open('D:/uw course/capstone/mypersonality/IRtest2.txt')#IR corpus
file1 = open('D:/uw course/capstone/mypersonality/ECtest2grams.txt')#candidate
file2 = open('D:/uw course/capstone/mypersonality/wordlist_lemma.txt')#keyword

file3 = open('D:/uw course/capstone/mypersonality/wordlist_1_expanded.txt','w')

total=0#to trace the process
candidatelist = file1.readline().split(",")
keywordlist = file2.readline().split(",")
candidatecount=[0]*len(candidatelist)
print(len(candidatelist))
keywordcount=[0]*len(keywordlist)
cooccur= [[0 for col in range(len(keywordlist))] for row in range(len(candidatelist))]
PMI=[[0 for col in range(len(keywordlist))] for row in range(len(candidatelist))]

'''-----PMI calculation------'''
while 1:
#while total<=127679:
    line=file.readline()
    if not line:
        break
    total+=1

    i=0
    j=0
    candidate=[0]*len(candidatelist)
    keyword=[0]*len(keywordlist)
    for w1 in candidatelist:
        print(w1)
        candidate[i]=line.count(w1)
        candidatecount[i]+=candidate[i]
        i+=1;
    for w2 in keywordlist:
        keyword[j]=line.count(w2)
        keywordcount[j]+=keyword[j]
        j+=1;
    for p in range(0,i-1):###may need debug for matrix demensions
        for q in range(0,j-1):
            if candidate[p]*keyword[q] >0:
                cooccur[p][q]+=min(candidate[p],keyword[q]) #!!!!!!!
#print(cooccur)
    for N in range(1,100):
        if total == math.floor(12767965*N*0.01):
            print('%d' %N)

for p in range(0,i-1):
    for q in range(0,j-1):
        if candidatecount[p]*keywordcount[q]*cooccur[p][q]>0:
            #PMI[p][q]=math.log(cooccur[p][q]/(candidatecount[p]*keywordcount[q]))
            PMI[p][q]=cooccur[p][q]/(candidatecount[p]*keywordcount[q])
        else:
            PMI[p][q]=0
#print(PMI)
'''--------------------------'''
Threshold = 0.1

for p in range(0,i-1):
    PMI_MAX = PMI[p][0]
    for q in range(1,j-1):
        a = PMI[p][q]
        if a>PMI_MAX:
            PMI_MAX=a
            
    if PMI_MAX > Threshold:
        if candidate[p] not in keywordlist:#caution! and need further consideration
            keywordlist.append(candidatelist[p])

file3.write('%s,' %keywordlist)

file.close()
file1.close()
file2.close()
file3.close()
