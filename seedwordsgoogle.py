from __future__ import division
'''version3 seed words algorithm'''
'''changed IR corpus to google----
input: a IR corpus, a expanding corpus(the candidate wordlist), a seed wordlist
output: a expanded seed wordlist
--------------'''

import math
import numpy as np
import timeit
start = timeit.default_timer()


file1 = open('D:/uw course/capstone/mypersonality/ECtest3_punctation_len3_freqover3.txt')#candidate
file2 = open('D:/uw course/capstone/mypersonality/wordlist_lemma.txt')#keyword

'''file3 = open('D:/uw course/capstone/mypersonality/wordlist_1gram_freqover10_IR2_21w_thre0.01.txt','w')
Threshold = 0.01'''

import urllib.request
import json


def hits(word1,word2=""):
    query = "http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q="
    if word2 == "":
        print(query+word1)
        results = urllib.request.urlopen(query + word1)
    else:
        #print(query + word1+"%20"+"AROUND(10)"+"%20"+word2)
        results = urllib.request.urlopen(query + word1+"%20"+"AROUND(10)"+"%20"+word2)
    encoding = results.headers.get_content_charset()
    json_res = json.loads(results.read().decode(encoding))
    google_hits=int(json_res['responseData']['cursor']['estimatedResultCount'])
    return google_hits



candidatelist = file1.readline().split(",")
keywordlist = file2.readline().split(",")
canl=len(candidatelist)
print(canl)
candidatecount=[0]*canl
keyl=len(keywordlist)-1#one more than real from wordlist because of additional , 
keywordcount=[0]*keyl
print(keyl)
cooccur= [[0 for col in range(keyl)] for row in range(canl)]
PMI=[[0 for col in range(keyl)] for row in range(canl)]

'''-----PMI calculation------'''
i=0
j=0
for w1 in candidatelist:
    w1=w1.replace(" ","%20")
    print(w1)
    try:
        candidatecount[i]=hits(w1)
        print(candidatecount[i])
    except ValueError:
        candidatecount[i]=0   
    i+=1;
for w2 in keywordlist[0:keyl]:
    w1=w1.replace(" ","%20")
    try:
        keywordcount[j]=hits(w2)
    except ValueError:
        keywordcount[j]=0   
    j+=1;
for p in range(0,canl):
    for q in range(0,keyl):
        cooccur = hits(candidatelist[p].replace(" ","%20"),keywordlist[q].replace(" ","%20"))
#print(cooccur)
#for progress print

for p in range(0,canl):
    for q in range(0,keyl):
        if candidatecount[p]*keywordcount[q]*cooccur[p][q]>0:
            #PMI[p][q]=math.log(cooccur[p][q]/(candidatecount[p]*keywordcount[q]))
            PMI[p][q]=cooccur[p][q]/(candidatecount[p]*keywordcount[q])
        else:
            PMI[p][q]=0
#print(PMI)
#print(keywordcount)
'''--------------------------'''
file3 = open('D:/uw course/capstone/mypersonality/wordlist_1gram_freqover3_Google_21w_thre0.01.txt','w')
Threshold = 0.01
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
                keywordlist.append([candidatelist[p],round(math.log(PMI_MAX*total),2), keywordlist[max_index]])
            

file3.write('%s' %keywordlist[22:])
file3.close()

file4 = open('D:/uw course/capstone/mypersonality/wordlist_1gram_freqover3_Google_21w_thre0.05.txt','w')
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

file5 = open('D:/uw course/capstone/mypersonality/wordlist_1gram_freqover3_Google_21w_thre0.001.txt','w')
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

file6 = open('D:/uw course/capstone/mypersonality/wordlist_1gram_freqover3_Google_21w_thre0.1.txt','w')
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
file6.close()

file.close()
file1.close()
file2.close()


elapsed = (timeit.default_timer() - start)
print(elapsed)
