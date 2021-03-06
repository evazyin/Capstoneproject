'''svm using different features'''
'''feature extraction: unigrams'''
import sys
sys.path.append("D:/uw course/capstone/nltk-3.0a3/")
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.decomposition import PCA
import numpy as np
from sklearn import svm
from sklearn import cross_validation
from math import sqrt
import timeit
start = timeit.default_timer()

from nltk.tokenize import word_tokenize
from LIWC import extractLIWCFeatures, readDictionary
import sys

#Returns as list of features for input document
def getLIWCFeatures(file):
    #with open(in_path, "r") as text:
        for line in file:
            #in_text = text.read()

            #Tokenizes
            tokens = word_tokenize(in_text)

            #Creates liwc dictionary based on where LIWC_English.txt is
            LIWCDic = readDictionary("./LIWC/LIWC_English.txt")
            liwcFeatures.append(extractLIWCFeatures(tokens, LIWCDic))
            
            return liwcFeatures

vectorizer = CountVectorizer(ngram_range=(1, 2),stop_words=None,min_df=1,binary=True)
transformer = TfidfTransformer()
pca=PCA(n_components=10)

file = open('D:/uw course/capstone/mypersonality/NostalCorpus.txt','r')
file1 = open('D:/uw course/capstone/mypersonality/NostalCorpusLabel.txt','r')
file2 = open('D:/uw course/capstone/mypersonality/feature-LDA.txt','r')
corpus=[]
LDA=[]
y=[]
for line in file:
    corpus.append(line)
for var in file1:
    y.append(int(var))
for var in file2:
    LDA.append(int(var))
LIWC = getLIWCFeatures(file)
X = vectorizer.fit_transform(corpus)
print(X.toarray())
X_tfidf = transformer.fit_transform(X.toarray())
print(X_tfidf.toarray())#spare to intense
X_pca = pca.fit_transform(X_tfidf.toarray())
print(X_pca)

X_tfidf = np.concatenate((X_tfidf.toarray(), np.transpose(LDA).reshape(len(LDA),1)),axis=1)
X_tfidf = np.concatenate((X_tfidf,LIWC),axis=1)
#clf=svm.SVC()#rbf kernel
clf=svm.LinearSVC(C=1)#linear kernel
#clf.fit(X.toarray(),np.transpose(y))
#cv=cross_validation.cross_val_score(clf,X.toarray(),np.transpose(y),scoring="mean_squared_error",cv=10)
#clf.fit(X_tfidf.toarray(),np.transpose(y))
#cv=cross_validation.cross_val_score(clf,X_tfidf.toarray(),np.transpose(y),scoring="mean_squared_error",cv=10)
clf.fit(X_tfidf,np.transpose(y))
cv=cross_validation.cross_val_score(clf,X_tfidf,np.transpose(y),scoring="accuracy",cv=10)
#clf.fit(X_pca,np.transpose(y))
#cv=cross_validation.cross_val_score(clf,X_pca,np.transpose(y),scoring="mean_squared_error",cv=10)
#rms=sqrt(abs(sum(cv)/10))
print(cv)

file.close()
file1.close()
file2.close()
elapsed = (timeit.default_timer() - start)

