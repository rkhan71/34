#the purpose of this code is to find every possible permutation of 4 unique numbers from 1-16 that add up to 34. 
#Note that different orders of numbers (such as 16,15,1,2 and 16,15,2,1) are stored separately because this will make a difference in the overall solution

import sqlite3

connect = sqlite3.connect('34.db')
cursor = connect.cursor()

#creating a table in the database to store all these permutations into
cursor.execute('CREATE TABLE lines (lnid INT PRIMARY KEY, fst INT, snd INT, thd INT, fth INT)')
nums = range(1,17)
sums = []
id = 1

#loop that creates every possible permutation of 4 numbers from 1-16 inclusive and puts those numbers into the list 'sum4'
for i in range(16):
    sum4 = [0,0,0,0]
    sum4[0] = nums[i]
    for j in range(16):
        sum4[1] = nums[j]
        for k in range(16):
            sum4[2] = nums[k]
            for l in range(16):
                sum4[3] = nums[l]
                #loop that goes through the list 'sum4' and makes sure there are no repeated numbers
                norepeat = True
                for n in range(4):
                    if sum4.count(sum4[n]) > 1:
                        norepeat = False
                        break
                #adding valid permutations into the database. Storing each number in the permutation separately so I can query the database more effectively
                #when finding a solution
                if sum(sum4) == 34 and norepeat:
                    cursor.execute(f'INSERT INTO lines VALUES ({id}, {sum4[0]}, {sum4[1]}, {sum4[2]}, {sum4[3]})')
                    id += 1
connect.commit()
connect.close()
