#This code uses the permutations of sums to 34 in the database 34.db to create single squares with 4 numbers on each edge that add up to 34.
#It then checks if the permutations from the database can be put onto the squares diagonally to create a solution to the problem.

import sqlite3

connect = sqlite3.connect('34.db')
cursor = connect.cursor()

#creating a table to put the solutions into. Storing the edges of the original square as strings and then storing the numbers at each point of the final
#solution as integers individually
cursor.execute('CREATE TABLE solutions (top VARCHAR, right VARCHAR, bottom VARCAHR, left VARCHAR, north INT, east INT, south INT, west INT)')

#going through every single row in the table lines and making it the first edge of the square
cursor.execute('SELECT * FROM lines')
allrows = cursor.fetchall()
for row in allrows:
    #storing the numbers that have been used in a list so that we can check and make sure not to re-use them
    usednums = (row[1], row[2], row[3], row[4])
    #finding all potential second edges and looping through them, do the same for potential third and fourth edges
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
                #finding all possible diagoanl edges going through the left and top edges of the square and looping through them. Do the same for all the other
                #diagonal edges
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
                                #once the final diagonal edge is found, that means a solution has been found and it is added to the database
                                cursor.execute(f"INSERT INTO solutions VALUES ('{row}', '{row2}', '{row3}', '{row4}', {edge[4]}, {edge2[4]}, {edge3[4]}, {edge4[4]})")
connect.commit()
connect.close()
