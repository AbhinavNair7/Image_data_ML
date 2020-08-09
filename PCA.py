import numpy as np


def PCA(X,m,K):

    covariance = (1/m)*np.matmul(np.transpose(X),X);
    [U , S , V] = np.linalg.svd(covariance);
    U_reduce = U[:,0:K]
    Z = np.matmul(X,U_reduce)
    X_rec = np.matmul(Z,np.transpose(U_reduce))

    var_retain = sum(S[0:K]/sum(S))
    #error = (sum(sum((abs(X - X_rec))**2)))/(sum(sum(X**2)))

    #print(Z.shape,var_retain)
    return(Z,var_retain)
