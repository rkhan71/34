# 34
Writing code to solve a mathematical problem involving overlapping squares whose edges all add up to 34. 

Here is a detailed description of the problem:
There are 16 'points' created by the two overlapping squares as shown in IMG-3346.jpg. The goal is to use each of the numbers from 1-16 inclusive only once at each point so that every edge on both squares adds up to 34. Referencing the image provided in IMG-3346.jpg, the points 1, 2, 4, and 5 create on type of edge while the points 15, 16, 2, and 3 create another type of edge. There are 8 edges in total.

My Dad was the one who initially showed me this problem. He told me that he wrote a computer program to solve this when he was younger, but due to the low specs of computers back then, the code took 3 days to run before he got an answer. I thought this would be a very easy problem to solve with the tools I have at my disposal today and quickly wrote the code in 'initial_idea.py' and let it run. After it didn't give me a solution in 10 minutes I stopped the code and calculated the actual magnitude of this problem. By randomly going through every arrangement of the number 1-16, the code would have to go through over 20 trillion permutations which could take hundreds of years to run.

I realized I would have to think a lot harder to create a more efficient solution for a problem of this size. This repository shows the code I wrote to create this more efficient solution using python and SQL.

The file lists.db contains an SQL database created with sqlite3 containing one table, lists, which looks like this:
CREATE TABLE lists (
fst int,
snd int,
thd int,
fth int
);

This table is built to contain every permutation of 4 numbers from 1-16 that add up to 34. The table is filled using the code in 'sql.py'
