import numpy as np
from sklearn import svm
from sklearn import cross_validation
from math import sqrt
import timeit

start = timeit.default_timer()

data=np.loadtxt('D:/uw course/CSS 590C big data/project/factorized2.txt')
y=data[:,0]
x=data[:,1:]

clf=svm.SVC()'''or svm.LinearSVC() for linear kernel svm'''
clf.fit(x,y)
cv=cross_validation.cross_val_score(clf,x,y,scoring="mean_squared_error",cv=10)
rms=sqrt(abs(sum(cv)/10))
print(rms)

elapsed = (timeit.default_timer() - start)


