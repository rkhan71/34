#The purpose of this code is to use the possible edges in the database lists.db to create squares that could be used in the solution. 
#These are single squares with 4 numbers on each edge that add up to 34.

import sqlite3

connect = sqlite3.connect('lists.db')
cursor = connect.cursor()
cursor.execute('SELECT * FROM lists')
allrows = cursor.fetchall()
id = 1
for row in allrows: #going through every single row in the table lists and making it the first edge of our square
    usednums = [row[1], row[2], row[3], row[4]] #storing the numbers that have been used in a list so that we can check and make sure not to re-use them
    cursor.execute(f'SELECT * FROM lists WHERE fst = {row[4]};') #finding all potential second edges (where the last number of the first edge is the first number of this edge)
    ln2 = cursor.fetchall()
    for row2 in ln2: #going through every potential second edge
        cursor.execute(f'SELECT * FROM lists WHERE fst = {row2[4]};') #finding potential third edges
        ln3 = cursor.fetchall()
        #if statement makes sure that there is at least one potential third edge for us to use and makes sure that the numbers in the second edge
        #have not already been used
        if len(ln3) > 0 and row2[2] not in usednums and row2[3] not in usednums and row2[4] not in usednums: 
            #MISTAKE: appending to the usednums list and not deleteting old values from it in each loop means that the list contains more numbers than it should which 
            #lead to millions of valid squares not being entered into the database
            usednums += [row2[2], row2[3], row2[4]]
            for row3 in ln3: 
                cursor.execute(f'SELECT * FROM lists WHERE fst = {row3[4]} AND fth = {row[1]};')
                ln4 = cursor.fetchall()
                if len(ln4) > 0 and row3[2] not in usednums and row3[3] not in usednums and row3[4] not in usednums:
                    usednums += [row3[2], row3[3], row3[4]]
                    for row4 in ln4:
                        #final if statement that makes sure the new numbers from the fourth and final edge have not already been used. If they haven't then
                        #a valid square has been created using the edges 'row', 'row2', 'row3', and 'row4'.
                        if row4[2] not in usednums and row4[3] not in usednums:
                            cursor.execute(f'INSERT INTO edges VALUES ({row[0]}, {row2[0]}, {row3[0]}, {row4[0]}, {id})')
                            id += 1
connect.commit()
connect.close()
