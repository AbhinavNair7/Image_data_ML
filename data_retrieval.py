import sqlite3
import numpy as np


def data_retrieval():

    conn = sqlite3.connect('img_database.sqlite')
    cur = conn.cursor()

    cur.execute('SELECT y_row FROM Data_y ORDER BY y_row DESC LIMIT 1')
    total_images = cur.fetchone()[0]

    cur.execute('SELECT COUNT(X_row) FROM Data_X WHERE X_row = 1')
    pixels = cur.fetchone()[0]


    cur.execute('SELECT y_val FROM Data_y')
    values = cur.fetchall()
    y = np.reshape(np.transpose(values),(total_images,3))

    cur.execute('SELECT X_val FROM Data_X')
    values = cur.fetchall()
    X = np.reshape(np.transpose(values),(total_images,pixels))

    cur.close()
    return(X,y)
