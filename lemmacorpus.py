#version1 4/14/2014 for data lemma
import codecs
import sys
sys.path.append("D:/uw course/capstone/nltk-3.0a3/")#necessary??
from nltk.stem import WordNetLemmatizer
wn=WordNetLemmatizer()
from nltk import word_tokenize

#file = codecs.open('D:/uw course/capstone/mypersonality/status_b.csv',errors='ignore')
file = codecs.open('D:/uw course/capstone/mypersonality/status_b.csv',errors='ignore')
file1 = open('D:/uw course/capstone/mypersonality/status_b_lemma.txt','w')

while 1:   
    line = file.readline()
    if not line:
        break
    
    lineStr = str( line, encoding='latin-1' )
    lineStr = lineStr.lower()
    #for my personality data only
    linelist = lineStr.split(",")
    lineStr1=','.join(linelist[2:])#in case the post part is also split
    #print(lineStr1)
    tokens = word_tokenize(lineStr1)
    lineStr2 = ' '.join(wn.lemmatize(w) for w in tokens) #similar for stem usage
    #print(lineStr2)
    #print(lineStr.find('is very'))
    file1.write(str(lineStr2.encode('latin-1')))
    file1.write('\n')

    del line
    del lineStr
    del lineStr1
    del lineStr2

file.close()
file1.close()

