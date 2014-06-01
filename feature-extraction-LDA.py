import sys
sys.path.append("D:/python/Lib/site-packages/gensim-0.10.0rc1/")
sys.path.append("D:/uw course/capstone/nltk-3.0a3/")
from gensim import corpora, models, similarities
from itertools import chain
import nltk
from nltk.corpus import stopwords
from operator import itemgetter
import re
from functools import reduce
import string

file = open('D:/uw course/capstone/mypersonality/NostalCorpusExpand.txt','r')
documents=[]
for line in file:
    line = reduce(lambda line,c: line.replace(c, ' '), string.punctuation, line)
    documents.append(line)

stoplist = stopwords.words('english')
texts = [[word for word in document.lower().split() if word not in stoplist]
 for document in documents]

dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]

tfidf = models.TfidfModel(corpus) 
corpus_tfidf = tfidf[corpus]

#lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=100)
#lsi.print_topics(20)

n_topics = 60
lda = models.LdaModel(corpus_tfidf, id2word=dictionary, num_topics=n_topics)

for i in range(0,949):
    feature_LDA=str(max(lda[corpus[i]],key=itemgetter(1))[0])
    print(feature_LDA)
file.close()
'''for i in range(0, n_topics):
 temp = lda.show_topic(i, 10)
 terms = []
 for term in temp:
     terms.append(term[1])
 #print("Top 10 terms for topic #" + str(i) + ": "+ ", ".join(terms))
 
#print 
print('Which LDA topic maximally describes a document?\n')
print('Original document: ' + documents[1])
print('Preprocessed document: ' + str(texts[1]))
print('Matrix Market format: ' + str(corpus[1]))
print('Topic probability mixture: ' + str(lda[corpus[1]]))
print('Maximally probable topic: topic #' + str(max(lda[corpus[1]],key=itemgetter(1))[0]))'''
