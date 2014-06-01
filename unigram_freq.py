'''For tokenize EC corpus and eliminate stopwords and puncations
extract unigrams with freq>k
4/29/2014 version2 
'''
import string
import sys
sys.path.append("D:/uw course/capstone/nltk-3.0a3/")#necessary??
import nltk
from nltk import word_tokenize
from functools import reduce

file = open('D:/uw course/capstone/mypersonality/IRtest3.txt','r')
file1 = open('D:/uw course/capstone/mypersonality/ECtest3_punctation_len3_freqover3.txt','w')
file2 = open('D:/uw course/capstone/mypersonality/stopwords_stem.txt','r')
stopwords=file2.readline().split(",")
#print(len(stopwords)) nltk.corpus.stopwords.words('english')
ECwordlist=[]

while 1:   
    line = file.readline()
    if not line:
        break

    tokens = word_tokenize(reduce(lambda line,c: line.replace(c, ' '), string.punctuation, line))
    #tokens = word_tokenize(reduce(lambda line,c: line.replace(c, ' '), '.,\~=', line))
    fdist = nltk.FreqDist(tokens)
    for w,v in fdist.items():
        #print(w,v)
        if w not in stopwords:
            if v <3:
                continue
            if w not in ECwordlist:
                if len(w)>=3:
                    ECwordlist.append(w)
                    #print(w)
                    file1.write("%s,"%w)

    

file.close()
file1.close()
file2.close()

