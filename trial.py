import numpy as np
from PIL import Image
import glob
from PCA import PCA


def trial_collect(folder,cancer_type,reduce=0,Old_X=None,Old_y=None):

    file = glob.glob('data/'+folder+'/*.tif')
    total_images = len(file)
    y = np.zeros((total_images,3))
    red_array = np.zeros((total_images,10000))
    #green_array = np.zeros((total_images,1443520))
    #blue_array = np.zeros((total_images,1443520))
    count = 0

    for img_name in file:
        img = Image.open(img_name)
        img_array = np.array(img)
        r_array = img_array[:,:,0]

        if reduce == 1:
            m = np.shape(r_array)[0]
            r_array = PCA(r_array,m,?)
            r_array = np.transpose(r_array)

            m = np.shape(r_array)[0]
            r_array = PCA(r_array,m,?)
            r_array = np.transpose(r_array)


        #g_array = img_array[:,:,1]
        #b_array = img_array[:,:,2]

        red_array[count,:] = np.concatenate((r_array),axis=None)
        #green_array[count,:] = np.concatenate((g_array),axis=None)
        #blue_array[count,:] = np.concatenate((b_array),axis=None)
        y[count,cancer_type-1] = 1


        count += 1
        print(str(count),'/',str(total_images))

    X = np.concatenate((red_array,green_array,blue_array),axis = 1)

    return(red_array,y,total_images)
