import sqlite3
from data_collection import data_collect


def store_data(X,y,X_table,y_table):

    total_images = X.shape[0]
    pixels = X.shape[1]

    conn = sqlite3.connect('img_database.sqlite')
    cur = conn.cursor()

    try:
        cur.execute('SELECT y_row FROM {} ORDER BY y_row DESC LIMIT 1'.format(y_table))
        last_row = cur.fetchone()[0]
        print('received last datapoint :',last_row)

    except:
        last_row = 0

    #query = 'SELECT * FROM {}'.format(X_table)
    #cur.execute(query)
    cur.execute('CREATE TABLE IF NOT EXISTS {}(X_row INTEGER, X_val INTEGER)'.format(X_table))
    cur.execute('CREATE TABLE IF NOT EXISTS {}(y_row INTEGER, y_val INTEGER)'.format(y_table))

    for i in range(1,total_images+1):
        for j in range(1,pixels+1):
            cur.execute('''INSERT INTO {}(X_row,X_val)
            VALUES (?,?)'''.format(X_table),(i+last_row,X[i-1,j-1]))
        for j in range(1,4):
            cur.execute('''INSERT INTO {}(y_row,y_val)
            VALUES (?,?)'''.format(y_table),(i+last_row,y[i-1,j-1]))
        conn.commit()
        print(i,'/',total_images)

    cur.close()
