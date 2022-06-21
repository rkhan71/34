import sqlite3

connect = sqlite3.connect('34.db')
cursor = connect.cursor()
cursor.execute('CREATE TABLE solutions (top VARCHAR, right VARCHAR, bottom VARCAHR, left VARCHAR, north INT, east INT, south INT, west INT)')
cursor.execute('SELECT * FROM lines')
allrows = cursor.fetchall()
for row in allrows:
    usednums = (row[1], row[2], row[3], row[4])
    cursor.execute(f'SELECT * FROM lines WHERE fst = {row[4]} AND snd NOT IN {usednums} AND thd NOT IN {usednums} AND fth NOT IN {usednums}')
    ln2 = cursor.fetchall()
    for row2 in ln2:
        usednums = (row[1], row[2], row[3], row[4], row2[2], row2[3], row2[4])
        cursor.execute(f'SELECT * FROM lines WHERE fst = {row2[4]} AND snd NOT IN {usednums} AND thd NOT IN {usednums} AND fth NOT IN {usednums}')
        ln3 = cursor.fetchall()
        for row3 in ln3:
            usednums = (row[1], row[2], row[3], row[4], row2[2], row2[3], row2[4], row3[2], row3[3], row3[4])
            cursor.execute(f'SELECT * FROM lines WHERE fst = {row3[4]} AND fth = {row[1]} AND snd NOT IN {usednums} AND thd NOT IN {usednums}')
            ln4 = cursor.fetchall()
            for row4 in ln4:
                usednums = (row[1], row[2], row[3], row[4], row2[2], row2[3], row2[4], row3[2], row3[3], row3[4], row4[2], row4[3])
                cursor.execute(f'SELECT * FROM lines WHERE fst NOT IN {usednums} AND snd = {row4[3]} AND thd = {row[2]} AND fth NOT IN {usednums}')
                edges = cursor.fetchall()
                for edge in edges:
                    usednums = (row[1], row[2], row[3], row[4], row2[2], row2[3], row2[4], row3[2], row3[3], row3[4], row4[2], row4[3], edge[1], edge[4])
                    cursor.execute(f'SELECT * FROM lines WHERE fst = {edge[4]} AND snd = {row[3]} AND thd = {row2[2]} AND fth NOT IN {usednums}')
                    edges2 = cursor.fetchall()
                    for edge2 in edges2:
                        usednums = (row[1], row[2], row[3], row[4], row2[2], row2[3], row2[4], row3[2], row3[3], row3[4], row4[2], row4[3], edge[1], edge[4], edge2[4])
                        cursor.execute(f'SELECT * FROM lines WHERE fst = {edge2[4]} AND snd = {row2[3]} AND thd = {row3[2]} AND fth NOT IN {usednums}')
                        edges3 = cursor.fetchall()
                        for edge3 in edges3:
                            cursor.execute(f'SELECT * FROM lines WHERE fst = {edge3[4]} AND snd = {row3[3]} AND thd = {row4[2]} AND fth = {edge[1]}')
                            edges4 = cursor.fetchall()
                            for edge4 in edges4:
                                cursor.execute(f"INSERT INTO solutions VALUES ('{row}', '{row2}', '{row3}', '{row4}', {edge[4]}, {edge2[4]}, {edge3[4]}, {edge4[4]})")
connect.commit()
connect.close()
