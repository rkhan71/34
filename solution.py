import sqlite3

connect = sqlite3.connect('lists.db')
cursor = connect.cursor()
cursor.execute('SELECT * FROM edges')
squares = cursor.fetchall()
rolex = 0
for sq in squares:
    cursor.execute(f'SELECT * FROM lists WHERE id = {sq[0]}')
    t = cursor.fetchone()
    cursor.execute(f'SELECT * FROM lists WHERE id = {sq[1]}')
    r = cursor.fetchone()
    cursor.execute(f'SELECT * FROM lists WHERE id = {sq[2]}')
    b = cursor.fetchone()
    cursor.execute(f'SELECT * FROM lists WHERE id = {sq[3]}')
    l = cursor.fetchone()
    #get lists of ids of square which contain edges that work
    cursor.execute(f'SELECT id FROM edges WHERE top IN (SELECT id FROM lists WHERE snd = {l[3]} AND thd = {t[2]});')
    tops = cursor.fetchall()
    tlist = []
    for top in tops:
        tlist += [top]
    cursor.execute(f'SELECT id FROM edges WHERE right IN (SELECT id FROM lists WHERE snd = {t[3]} AND thd = {r[2]});')
    rights = cursor.fetchall()
    rlist = []
    for right in rights:
        rlist += [right]
    cursor.execute(f'SELECT id FROM edges WHERE top IN (SELECT id FROM lists WHERE snd = {r[3]} AND thd = {b[2]});')
    bottoms = cursor.fetchall()
    blist = []
    for bottom in bottoms:
        blist += [bottom]
    cursor.execute(f'SELECT id FROM edges WHERE top IN (SELECT id FROM lists WHERE snd = {b[3]} AND thd = {l[2]});')
    lefts = cursor.fetchall()
    llist = []
    for left in lefts:
        llist += [left]
    #make sure no lists are empty
    if tlist and rlist and blist and llist:
        #find intersect of lists
        intersect = list(set(tlist) & set(rlist) & set(blist) & set(llist))
        #make sure intersect is not empty then check that the chosen squares have no duplicate numbers and if so add them to the database
        if intersect:
            for sqid in intersect:
                cursor.execute(f'SELECT fst, snd, thd, fth FROM lists WHERE id = (SELECT top FROM edges WHERE id = {sqid})')
                tope = cursor.fetchone()
                cursor.execute(f'SELECT fst, snd, thd, fth FROM lists WHERE id = (SELECT bottom FROM edges WHERE id = {sqid})')
                bottome = cursor.fetchone()
                fsquare = t + r + b + l
                if tope[0] not in fsquare and tope[3] not in fsquare and bottome[0] not in fsquare and bottome[3] not in fsquare:
                    cursor.execute(f'INSERT INTO solutions VALUES ({sq[4]}, {sqid})')
connect.commit()
connect.close()
