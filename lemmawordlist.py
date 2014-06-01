#version1 for wordlist lemma 4/14/2014
import sys
sys.path.append("D:/uw course/capstone/nltk-3.0a3/")#necessary??
from nltk.stem import WordNetLemmatizer
wn=WordNetLemmatizer()
from nltk import word_tokenize

file = open('D:/uw course/capstone/mypersonality/wordlist.txt')
file1 = open('D:/uw course/capstone/mypersonality/wordlist_lemma.txt','w')
keywordstr = file.readline()
keywordlist = keywordstr.split(",")
for word in keywordlist:
    tokens = word_tokenize(word)
    keyword =' '.join(wn.lemmatize(w) for w in tokens)
    print(keyword)
    file1.write('%s,' %keyword)

file1.close()
file.close()

