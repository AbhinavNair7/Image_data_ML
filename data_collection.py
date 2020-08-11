import numpy as np
from PIL import Image
import glob


def data_collect(folder,cancer_type,Old_X=None,Old_y=None):

    file = glob.glob('data/'+folder+'/*.tif')
    total_images = len(file)
    count = 0

    for img_name in file:
        img = Image.open(img_name)
        img_array = np.array(img)
        red_array = img_array[:,:,0]
        green_array = img_array[:,:,1]
        blue_array = img_array[:,:,2]

        if count == 0:
            pixels = img_array.shape[0]*img_array.shape[1]*3
            X = np.zeros((total_images,pixels))
            y = np.zeros((total_images,3))

        X[count,:] = np.concatenate((red_array,green_array,blue_array),axis = None)
        y[count,cancer_type-1] = 1

        count += 1
        print(str(count),'/',str(total_images))

    if type(Old_X) == type(X):
        X = np.concatenate((Old_X,X),axis=0)
        y = np.concatenate((Old_y,y),axis=0)


    return(X,y,total_images,pixels)
