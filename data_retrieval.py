import sqlite3
import numpy as np


def data_retrieval(data_type):

    table_name = {'train':['X_train_Data','y_train_Data'],'CV':['X_CV_Data','y_CV_Data'],'test':['X_test_Data','y_test_Data']}

    for key,value in table_name.items():
        if data_type == key:
            X_table = value[0]
            y_table = value[1]

    conn = sqlite3.connect('img_database.sqlite')
    cur = conn.cursor()

    cur.execute('SELECT y_row FROM {} ORDER BY y_row DESC LIMIT 1'.format(y_table))
    total_images = cur.fetchone()[0]

    cur.execute('SELECT COUNT(X_row) FROM {} WHERE X_row = 1'.format(X_table))
    pixels = cur.fetchone()[0]

    cur.execute('SELECT y_val FROM {}'.format(y_table))
    values = cur.fetchall()
    y = np.reshape(np.transpose(values),(total_images,3))

    cur.execute('SELECT X_val FROM {}'.format(X_table))
    values = cur.fetchall()
    X = np.reshape(np.transpose(values),(total_images,pixels))

    cur.close()
    return(X,y)
