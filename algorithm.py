import numpy as np
import sklearn
from sklearn.linear_model import LogisticRegression
from data_retrieval import data_retrieval

X,y = data_retrieval(113,10000)

lmbda = 1
model = LogisticRegression(max_iter=100,C = 1/lmbda)
fit = model.fit(X,y[:,0])
acc = model.score(X,y[:,0])
coef = model.coef_
intercept1 = model.intercept_

print(acc)
print(coef,intercept1)
