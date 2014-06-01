'''For tokenize EC corpus and eliminate stopwords and puncations
4/29/2014 version2 
'''
import string
import sys
sys.path.append("D:/uw course/capstone/nltk-3.0a3/")#necessary??
from nltk import word_tokenize
from functools import reduce

file = open('D:/uw course/capstone/mypersonality/IRtest3.txt','r')
file1 = open('D:/uw course/capstone/mypersonality/ECtest3_punctation_len3_freqover0.txt','w')
file2 = open('D:/uw course/capstone/mypersonality/stopwords.txt','r')
stopwords=file2.readline().split(",")
#print(len(stopwords)) nltk.corpus.stopwords.words('english')
ECwordlist=[]

while 1:   
    line = file.readline()
    if not line:
        break

    tokens = word_tokenize(reduce(lambda line,c: line.replace(c, ' '), string.punctuation, line))
    #tokens = word_tokenize(reduce(lambda line,c: line.replace(c, ' '), '.,\~=', line))

    for w in tokens[1:]: 
        if w not in stopwords:
            if w not in ECwordlist:
                #if len(w)>=3:
                    ECwordlist.append(w)
                    #print(w)
                    file1.write("%s,"%w)

    

file.close()
file1.close()
file2.close()
