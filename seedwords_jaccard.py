'''version5 seed words algorithm using jaccard 05/11'''
'''changed the near metric to jaccard distance ----
input: a IR corpus, a expanding corpus(the candidate wordlist), a seed wordlist
output: a expanded seed wordlist
--------------'''
import math
import numpy as np
import timeit
start = timeit.default_timer()

file = open('D:/uw course/capstone/mypersonality/IRtest2.txt')#IR corpus
file1 = open('D:/uw course/capstone/mypersonality/ECtest3_punctation_len3_freqover3.txt')#candidate
file2 = open('D:/uw course/capstone/mypersonality/wordlist_lemma.txt')#keyword

'''file3 = open('D:/uw course/capstone/mypersonality/wordlist_1gram_freqover10_IR2_21w_thre0.01.txt','w')
Threshold = 0.01'''

total=0#to trace the process
candidatelist = file1.readline().split(",")
keywordlist = file2.readline().split(",")
canl=len(candidatelist)
print(canl)
candidatecount=[0]*canl
keyl=len(keywordlist)-1#one more than real from wordlist because of additional , 
#keywordcount=[0]*keyl
print(keyl)
cooccur= [[0 for col in range(keyl)] for row in range(canl)]
PMI=[[0 for col in range(keyl)] for row in range(canl)]

'''-----PMI calculation------'''
while 1:
#while total<=127679:
    line=file.readline()
    if not line:
        break
    total+=1

    i=0
    j=0
    for w1 in candidatelist:
        #print(w1)
        if w1 in line:
            candidatecount[i]+=1
            #print(w1)
            for q in range(0,keyl):
                cooccur[i][q]=cooccur[i][q]+0.5
        i+=1;
    for w2 in keywordlist[0:keyl]:
        if w2 in line:
            #keywordcount[j]+=1
            for p in range(0,canl):
                cooccur[p][j]=cooccur[p][j]+0.5
        j+=1;
    #print(cooccur)
    cooccur=np.floor(cooccur)
    #print(cooccur)
    #for progress print
    for N in range(1,100):
        if total == math.floor(12767965*N*0.01):
            print('%d' %N)

for p in range(0,canl):
    for q in range(0,keyl):
        if candidatecount[p]*keywordcount[q]*cooccur[p][q]>0:
            #PMI[p][q]=math.log(cooccur[p][q]/(candidatecount[p]*keywordcount[q]))
            PMI[p][q]=cooccur[p][q]/candidatecount[p]
        else:
            PMI[p][q]=0
print(PMI)
#print(keywordcount)
'''--------------------------'''
file3 = open('D:/uw course/capstone/mypersonality/wordlist_test.txt','w')
Threshold = 0.01
keywordlist1 = []
for p in range(0,canl):
    PMI_MAX = PMI[p][0]
    max_index = 0;
    for q in range(1,keyl):
        a = PMI[p][q]
        if a > PMI_MAX:
            PMI_MAX = a
            max_index = q
            
    if PMI_MAX > Threshold:
        if candidatelist[p] not in keywordlist:#caution! and need further consideration
            if (candidatelist[p].find("i ")==-1) & (candidatelist[p].find("you ")==-1) & (candidatelist[p].find(" and")==-1) & (candidatelist[p].find("and ")==-1) :
                keywordlist1.append([candidatelist[p],round(math.log(PMI_MAX*total),2), keywordlist[max_index]])
            

file3.write('%s' %keywordlist1)
file3.close()

'''file4 = open('D:/uw course/capstone/mypersonality/wordlist_3gram_freqover10_IR2(nostalIR)_13w_thre0.05.txt','w')
Threshold = 0.05
keywordlist2 = []
for p in range(0,canl):
    PMI_MAX = PMI[p][0]
    max_index = 0;
    for q in range(1,keyl):
        a = PMI[p][q]
        if a > PMI_MAX:
            PMI_MAX = a
            max_index = q
            
    if PMI_MAX > Threshold:
        if candidatelist[p] not in keywordlist:#caution! and need further consideration
            if (candidatelist[p].find("i ")==-1) & (candidatelist[p].find("you ")==-1) & (candidatelist[p].find(" and")==-1) & (candidatelist[p].find("and ")==-1) :
                keywordlist2.append([candidatelist[p],round(math.log(PMI_MAX*total),2), keywordlist[max_index]])
            

file4.write('%s' %keywordlist2)
file4.close()

file5 = open('D:/uw course/capstone/mypersonality/wordlist_3gram_freqover10_IR2(nostalIR)_13w_thre0.001.txt','w')
Threshold = 0.001
keywordlist3 = []
for p in range(0,canl):
    PMI_MAX = PMI[p][0]
    max_index = 0;
    for q in range(1,keyl):
        a = PMI[p][q]
        if a > PMI_MAX:
            PMI_MAX = a
            max_index = q
            
    if PMI_MAX > Threshold:
        if candidatelist[p] not in keywordlist:#caution! and need further consideration
            if (candidatelist[p].find("i ")==-1) & (candidatelist[p].find("you ")==-1) & (candidatelist[p].find(" and")==-1) & (candidatelist[p].find("and ")==-1) :
                keywordlist3.append([candidatelist[p],round(math.log(PMI_MAX*total),2), keywordlist[max_index]])
            

file5.write('%s' %keywordlist3)
file5.close()

file6 = open('D:/uw course/capstone/mypersonality/wordlist_3gram_freqover10_IR2(nostalIR)_13w_thre0.1.txt','w')
Threshold = 0.1
keywordlist4 = []
for p in range(0,canl):
    PMI_MAX = PMI[p][0]
    max_index = 0;
    for q in range(1,keyl):
        a = PMI[p][q]
        if a > PMI_MAX:
            PMI_MAX = a
            max_index = q
            
    if PMI_MAX > Threshold:
        if candidatelist[p] not in keywordlist:#caution! and need further consideration
            if (candidatelist[p].find("i ")==-1) & (candidatelist[p].find("you ")==-1) & (candidatelist[p].find(" and")==-1) & (candidatelist[p].find("and ")==-1) :
                keywordlist4.append([candidatelist[p],round(math.log(PMI_MAX*total),2), keywordlist[max_index]])
            

file6.write('%s' %keywordlist4)
file6.close()'''

file.close()
file1.close()
file2.close()


elapsed = (timeit.default_timer() - start)
print(elapsed)
