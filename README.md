# 34
Writing code to solve a mathematical problem involving overlapping squares whose edges all add up to 34. 

Here is a detailed description of the problem:
There are 16 'points' created by the two overlapping squares as shown in IMG-3346.jpg. The goal is to use each of the numbers from 1-16 inclusive only once at each point so that every edge on both squares adds up to 34. Referencing the image provided in IMG-3346.jpg, the points 1, 2, 4, and 5 create on type of edge while the points 15, 16, 2, and 3 create another type of edge. There are 8 edges in total.

My Dad was the one who initially showed me this problem. He told me that he wrote a computer program to solve this when he was younger, but due to the low specs of computers back then, the code took 3 days to run before he got an answer. I thought this would be a very easy problem to solve with the tools I have at my disposal today and quickly wrote the code in 'initial_idea.py' and let it run. After it didn't give me a solution in 10 minutes I stopped the code and calculated the actual magnitude of this problem. By randomly going through every arrangement of the number 1-16, the code would have to go through over 20 trillion permutations which could take hundreds of years to run.

I realized I would have to think a lot harder to create a more efficient solution for a problem of this size. This repository shows the code I wrote to create this more efficient solution using python and SQL.

The database lists.db created with sqlite3 contians three tables: lists, edges, and solutions, which look like this:
CREATE TABLE lists (
id int,
fst int,
snd int,
thd int,
fth int
);

This table is built to contain every permutation of 4 numbers from 1-16 that add up to 34. The table is filled using the code in 'sql.py'

CREATE TABLE edges (
top int,
right int,
bottom int,
left int,
id int
);

This table is built to contain all the valid single squares that could be made from the numbers in the tables lists. Valid single squares contain 12 unique numbers (4 on each edge with the numbers on the corners used for 2 different edges), and all edges add up to 34. The column for each edge contains the id to a permutation of 4 numbers from lists. The table is filled using the code in 'square.py'.

CREATE TABLE solutions (
square1 int,
square2 int
);

This table is built to contain the id to two squares from the table edges which overlap and produce a solution to the overall problem. An attempt at the code to fill this table was written in the file 'solution.py' however it does not work at the moment.

