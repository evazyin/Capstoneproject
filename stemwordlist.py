#version1 for wordlist stem 4/22/2014
import sys
sys.path.append("D:/uw course/capstone/nltk-3.0a3/")#necessary??
from nltk.stem.lancaster import LancasterStemmer
st=LancasterStemmer()
from nltk import word_tokenize

#file = open('D:/uw course/capstone/mypersonality/wordlist.txt')
file = open('D:/uw course/capstone/mypersonality/stopwords.txt')
#file1 = open('D:/uw course/capstone/mypersonality/wordlist_stem.txt','w')
file1 = open('D:/uw course/capstone/mypersonality/stopwords_stem.txt','w')
keywordstr = file.readline()
keywordlist = keywordstr.split(",")
for word in keywordlist:
    tokens = word_tokenize(word)
    keyword =' '.join(st.stem(w) for w in tokens)
    print(keyword)
    file1.write('%s,' %keyword)

file1.close()
file.close()

