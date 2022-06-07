#the purpose of this code is to find every possible edge that can be used to create a solution. This is done by finding every permutation of 4 unique numbers 
#from 1-16 that add up to 34. Note that different orders of numbers (such as 16,15,1,2 and 16,15,2,1) are stored separately because this will make a difference in the
#overall solution

import sqlite3

#connecting to database 'lists.db' which has already been created using sqlite3 and contains one table 'lists' with 4 columns
connect = sqlite3.connect('lists.db')
cursor = connect.cursor()
nums = range(1,17)
sums = []

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
                #a loop that goes through the list 'sum4' and makes sure there are no repeated numbers
                norepeat = True
                for n in range(4):
                    if sum4.count(sum4[n]) > 1:
                        norepeat = False
                        break
                #if there are no repeated numbers and the numbers in sum4 add up to 34, this is a possible edge for our solution so each number
                #from the current version of sum4 is stored into the table lists in a particular order
                if sum(sum4) == 34 and norepeat:
                    cursor.execute(f'INSERT INTO lists VALUES ({sum4[0]}, {sum4[1]}, {sum4[2]}, {sum4[3]});')
connect.commit()
connect.close()
