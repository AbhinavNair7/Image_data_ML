import numpy as np
from data_storage import store_data


def randomise_and_store(X,y,train_ratio,CV_ratio=0):

    m = X.shape[0]
    n = X.shape[1]

    data_matrix = np.concatenate((X,y),axis=1)
    np.random.shuffle(data_matrix)

    X_random = data_matrix[:,0:n].reshape(X.shape)
    y_random = data_matrix[:,n:n+3].reshape(y.shape)

    X_train = X_random[0:round(train_ratio*m),:]
    y_train = y_random[0:round(train_ratio*m),:]
    store_data(X_train,y_train,'X_train_Data','y_train_Data')

    if CV_ratio != 0 :

        X_CV = X_random[round(train_ratio*m):round((train_ratio+CV_ratio)*m),:]
        y_CV = y_random[round(train_ratio*m):round((train_ratio+CV_ratio)*m),:]
        store_data(X_CV,y_CV,'X_CV_Data','y_CV_Data')

    X_test = X_random[round((train_ratio+CV_ratio)*m):m,:]
    y_test = y_random[round((train_ratio+CV_ratio)*m):m,:]
    store_data(X_test,y_test,'X_test_Data','y_test_Data')
