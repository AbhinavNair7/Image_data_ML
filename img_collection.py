import numpy as np
from PIL import Image
from PCA import PCA

def img_collect(img_name):
    img = Image.open(img_name)
    img_array = np.array(img)
    new_array = np.zeros((800,70,3))

    for i in range(3):
        array = np.transpose(img_array[:,:,i])
        m = np.shape(array)[0]
        array,*extra = PCA(array,m,800)
        array = np.transpose(array)

        m = np.shape(array)[0]
        new_array[:,:,i],*extra = PCA(array,m,70)

    X = np.zeros((1,168000))
    X[0,:] = np.concatenate((new_array[:,:,0],new_array[:,:,1],new_array[:,:,2]),axis=None)

    return(X)
