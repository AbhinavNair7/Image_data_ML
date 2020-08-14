import sqlite3
import  numpy as np
import math


def store_data(X,y,X_table,y_table):

    total_images = X.shape[0]
    pixels = X.shape[1]

    if total_images > 999:
        print('too many images, need upgrade')
        exit()

    conn = sqlite3.connect('img_database.sqlite')
    cur = conn.cursor()

    try:
        cur.execute('SELECT Count(*) FROM {}'.format(y_table))
        last_row = cur.fetchone()[0]
        cur.execute('ALTER TABLE {} RENAME TO Old_X'.format(X_table))
        print('received last datapoint :',last_row)

    except:
        last_row = 0

    cur.execute('CREATE TABLE X(img{} INTEGER)'.format(last_row+1))
    cur.execute('CREATE TABLE y(col1 INTEGER,col2 INTEGER,col3 INTEGER)')
    last_row += 1

    for i in range(last_row+1,last_row+total_images):

        column_name = 'img'+str(i)
        cur.execute('ALTER TABLE X ADD {}'.format(column_name))

    conn.commit()

    grp_quantity = math.floor(999/total_images)
    grp_enteries = math.floor(pixels/grp_quantity)
    remainder = pixels%grp_quantity

    sql_part1 = ',?'*(total_images-1)
    sql_part2 = ',(?'+sql_part1+')'
    old_range = 0

    if grp_enteries == 0 and remainder != 0:
        insert_X = np.concatenate(np.transpose(X[:,0:pixels]))
        cur.execute('INSERT INTO X VALUES (?{}){}'.format(sql_part1,sql_part2*(remainder-1)),(insert_X))

    for j in range(1,grp_enteries+1):
        new_range = j*grp_quantity
        insert_X = np.concatenate(np.transpose(X[:,old_range:new_range]))

        cur.execute('INSERT INTO X VALUES (?{}){}'.format(sql_part1,sql_part2*(grp_quantity-1)),(insert_X))
        old_range = new_range

        if j == grp_enteries and remainder != 0:
            insert_X = np.concatenate(np.transpose(X[:,new_range:pixels]))
            cur.execute('INSERT INTO X VALUES (?{}){}'.format(sql_part1,sql_part2*(remainder-1)),(insert_X))

        conn.commit()

        print(j,'/',grp_enteries)

    for j in range(0,total_images):
        cur.execute('INSERT INTO y(col1,col2,col3) VALUES(?,?,?)',(y[j,:]))
        conn.commit()

    if last_row > 1:
        cur.execute('CREATE TABLE {} AS SELECT Old_X.*, X.* FROM X LEFT JOIN Old_X ON Old_X.rowid = X.rowid'.format(X_table))
        cur.execute('INSERT INTO {} SELECT*FROM y'.format(y_table))
        cur.execute('DROP TABLE Old_X')
        cur.execute('DROP TABLE X')
        cur.execute('DROP TABLE y')

    else:
        cur.execute('ALTER TABLE X RENAME TO {}'.format(X_table))
        cur.execute('ALTER TABLE y RENAME TO {}'.format(y_table))

    conn.commit()
    cur.close()
