import numpy as np
from data_storage import store_data
from trial import trial_collect
from data_retrieval import data_retrieval

X,y,m = trial_collect('CLL',1,1)
#store_data(X,y,m,10000)
#X,y = data_retrieval(113,10000)
#print(X)

#a = np.array([[1,2,3],[4,5,6]])
#b = np.array([[1,2,3],[4,5,6]])
