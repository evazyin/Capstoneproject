'''generate n-grams'''
'''Version 1 put all lines into one line for calculating frequency for filtering
Version 2 for n grams, Version 3 do not have any filtering and repeated but memory saving'''
import sys
sys.path.append("D:/uw course/capstone/nltk-3.0a3/")
import nltk
from nltk.collocations import *
from nltk import word_tokenize
from functools import reduce
import string

file = open('D:/uw course/capstone/mypersonality/IRtest3.txt','r')
file1 = open('D:/uw course/capstone/mypersonality/ECtest3_3grams_freqover0.txt','w')
line=""
for val in file:
    line += val[1:]
tokens = word_tokenize(reduce(lambda line,c: line.replace(c, ' '), string.punctuation, line))


#finder = BigramCollocationFinder.from_words(tokens)
finder = TrigramCollocationFinder.from_words(tokens)

#finder.apply_freq_filter(10)#seems not perfrom well
#bigram_measures = nltk.collocations.BigramAssocMeasures()
#print(finder.nbest(bigram_measures.likelihood_ratio, 10))
for k,v in finder.ngram_fd.items():#use FreqDist actually
    i=0;
    if v <0:
        break#as the result of BigramC... is top-down sorting
    for w in k:
        file1.write("%s"%w)
        i=i+1;
        if i < len(k):
            file1.write(" ")
    file1.write(",")
file.close()
file1.close()
 
'''from nltk.util import ngrams
sentence = 'this is a foo bar sentences and i want to ngramize it'
n = 6
sixgrams = ngrams(sentence.split(), n)
for grams in sixgrams:
  print grams'''

'''import sys
sys.path.append("D:/uw course/capstone/nltk-3.0a3/")
import nltk
from nltk import bigrams
import string
from nltk import word_tokenize
from functools import reduce

file = open('D:/uw course/capstone/mypersonality/IRtest2.txt','r')
file1 = open('D:/uw course/capstone/mypersonality/ECtest2grams.txt','w')
ECwordlist=[]
while 1:   
    line = file.readline()
    if not line:
        break

    tokens = word_tokenize(reduce(lambda line,c: line.replace(c, ' '), string.punctuation, line))
    string_bigrams = bigrams(tokens[1:])
    for grams in string_bigrams:
      #print(reduce(lambda grams,c: str(grams).replace(c, ' '), string.punctuation, grams))
        #print(grams)
        ECwordlist.append(grams)
        i=0;
        for w in grams:
            file1.write("%s"%w)
            i=i+1;
            if i < len(grams):
                file1.write(" ")
        file1.write(",")

file.close()
file1.close()'''
