import sqlite3

connect = sqlite3.connect('34.db')
cursor = connect.cursor()
cursor.execute('CREATE TABLE lines (lnid INT PRIMARY KEY, fst INT, snd INT, thd INT, fth INT)')
nums = range(1,17)
sums = []
id = 1
for i in range(16):
    sum4 = [0,0,0,0]
    sum4[0] = nums[i]
    for j in range(16):
        sum4[1] = nums[j]
        for k in range(16):
            sum4[2] = nums[k]
            for l in range(16):
                sum4[3] = nums[l]
                norepeat = True
                for n in range(4):
                    if sum4.count(sum4[n]) > 1:
                        norepeat = False
                        break
                if sum(sum4) == 34 and norepeat:
                    cursor.execute(f'INSERT INTO lines VALUES ({id}, {sum4[0]}, {sum4[1]}, {sum4[2]}, {sum4[3]})')
                    id += 1
connect.commit()
connect.close()
