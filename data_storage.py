import sqlite3
from data_collection import data_collect


def store_data(X,y,total_images,pixels):

    conn = sqlite3.connect('img_database.sqlite')
    cur = conn.cursor()

    try:
        cur.execute('SELECT y_row FROM Data_y ORDER BY y_row DESC LIMIT 1')
        last_row = cur.fetchone()[0]

    except:
        last_row = 0

    cur.execute('CREATE TABLE IF NOT EXISTS Data_X(X_row INTEGER, X_val INTEGER)')
    cur.execute('CREATE TABLE IF NOT EXISTS Data_y(y_row INTEGER, y_val INTEGER)')

    for i in range(1,total_images+1):
        for j in range(1,pixels+1):
            cur.execute('''INSERT INTO Data_X(X_row,X_val)
            VALUES (?,?)''',(i+last_row,X[i-1,j-1]))
        for j in range(1,4):
            cur.execute('''INSERT INTO Data_y(y_row,y_val)
            VALUES (?,?)''',(i+last_row,y[i-1,j-1]))
        conn.commit()
        print(i,'/',total_images)

    cur.close()
