import sqlite3
import numpy as np

def data_retrieval(total_images,pixels):

    conn = sqlite3.connect('img_database.sqlite')
    cur = conn.cursor()

    X = np.zeros((total_images,pixels))
    y = np.zeros((total_images,3))

    for i in range(1,total_images+1):
        cur.execute('SELECT y_val FROM Data_y WHERE y_row = ?',(i,))
        val = cur.fetchall()
        for j in range(1,4):
            y[i-1,j-1] = val[j-1][0]


    for i in range(1,total_images+1):
        cur.execute('SELECT X_val FROM Data_X WHERE X_row = ?',(i,))
        val = cur.fetchall()
        for j in range(1,pixels+1):
            X[i-1,j-1] = val[j-1][0]

        print(i,'/',total_images)

    cur.close()
    return(X,y)
