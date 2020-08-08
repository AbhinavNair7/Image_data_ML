import numpy as np


def PCA(X,m,k):

    covariance = (1/m)*np.matmul(np.transpose(X),X);
    [U , S , V] = np.linalg.svd(covariance);
    U_reduce = U[:,0:k]
    Z = np.matmul(X,U_reduce)
    X_rec = np.matmul(Z,np.transpose(U_reduce))
    #print(Z)
    #print(X_rec)

    error1 = 1-sum(S)/sum(S[0:k])
    error2 = (sum(sum((X - X_rec)**2)))/(sum(sum(X**2)))
    print(Z.shape,error1,error2)

    return(Z)
