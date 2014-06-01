'''version2
1 read in a list of keyword
2 add post lemma and keyword lemma(in another file)
3 all posts to lower case
'''
import codecs

#revised 4/14/2014 add word lemma
import sys
sys.path.append("D:/uw course/capstone/nltk-3.0a3/")#necessary??
from nltk.stem import WordNetLemmatizer
wn=WordNetLemmatizer()
from nltk import word_tokenize

#file = codecs.open('D:/uw course/capstone/mypersonality/status_b.csv',errors='ignore')
file = codecs.open('C:/Downloads/fb_status_a.csv',errors='ignore')
file1 = open('D:/uw course/capstone/mypersonality/wordlist_lemma.txt')

total = -1 #header only status_a.csv have one line for header
nostalgic = 0
keywordstr = file1.readline()
keywordlist = keywordstr.split(",")
#print(keywordlist[1])

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

    defaultsenti = 0
    for i in range(0,len(keywordlist)-1):
        if lineStr2.find(keywordlist[i])>-1:
            defaultsenti+=1
    if defaultsenti > 0:
        nostalgic+=1
    total+=1


    '''if (lineStr.find('do you remember when')>-1)|(lineStr.find('down memory lane')>-1)|(lineStr.find('flashback')>-1)|(lineStr.find('go back in time')>-1)|(lineStr.find('good old days')>-1)|(lineStr.find('I miss those days')>-1)|(lineStr.find('nostalgic')>-1)|(lineStr.find('recollect')>-1)|(lineStr.find('redolent of')>-1)|(lineStr.find('relive the past')>-1)|(lineStr.find('reminiscent')>-1)|(lineStr.find('when we were younger')>-1)|(lineStr.find('those were the days')>-1):
        nostalgic+=1
    total+=1'''
    #file1.write('%d %d\n' %(total, nostalgic))
    
    '''print(total)
    print(lineStr)
    if nostalgic == 1:
        break'''
    
    del line
    del lineStr

file.close()
file1.close()
print(total)
print(nostalgic)




