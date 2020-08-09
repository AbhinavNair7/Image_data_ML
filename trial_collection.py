import numpy as np
from PIL import Image
import glob
from PCA import PCA
import time


def trial_collect(folder,cancer_type,Old_X=None,Old_y=None):

    file = glob.glob('data/'+folder+'/*.tif')
    total_images = len(file)
    X = np.zeros((total_images,168000))
    y = np.zeros((total_images,3))
    count = 0

    for img_name in file:
        img = Image.open(img_name)
        img_array = np.array(img)
        new_array = np.zeros((800,70,3))

        if count == 0 or count == 49 or count == 99:
            start_time = time.time()

        for i in range(3):
            array = np.transpose(img_array[:,:,i])
            m = np.shape(array)[0]
            array,*extra = PCA(array,m,800)
            array = np.transpose(array)

            m = np.shape(array)[0]
            new_array[:,:,i],*extra = PCA(array,m,70)

        X[count,:] = np.concatenate((new_array[:,:,0],new_array[:,:,1],new_array[:,:,2]),axis=None)
        y[count,cancer_type-1] = 1

        count += 1

        if count == 1 or count == 50 or count == 100:
            print(str(count),'/',str(total_images))
            end_time = time.time()
            print((end_time-start_time)*(total_images-count)/60,'mins left')

    return(X,y,total_images)
