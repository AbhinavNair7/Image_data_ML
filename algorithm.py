import numpy as np
import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from data_retrieval import data_retrieval

X,y = data_retrieval()
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)


lmbda = 0.1

model = LogisticRegression(max_iter=500,C = 1/lmbda)
fit = model.fit(X_train,y_train[:,0])
acc = model.score(X_test,y_test[:,0])

print('Accuracy :',acc)
# 60% accuracy
