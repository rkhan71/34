# 34
Writing code to solve a mathematical problem involving overlapping squares whose edges all add up to 34. 

Here is a detailed description of the problem:
There are 16 'points' created by the two overlapping squares as shown in IMG-3346.jpg. The goal is to use each of the numbers from 1-16 inclusive only once at each point so that every edge on both squares adds up to 34. Referencing the image provided in IMG-3346.jpg, the points 1, 2, 4, and 5 create on type of edge while the points 15, 16, 2, and 3 create another type of edge. There are 8 edges in total.

![alt text](https://github.com/rkhan71/34/blob/main/IMG-3346.jpg?raw=true)

My Dad was the one who initially showed me this problem. He told me that he wrote a computer program to solve this when he was younger, but due to the low specs of computers back then, the code took 3 days to run before he got an answer. I thought this would be a very easy problem to solve with the tools I have at my disposal today and quickly wrote the code in 'initial_idea.py' and let it run. After it didn't give me a solution in 10 minutes I stopped the code and calculated the actual magnitude of this problem. By randomly going through every arrangement of the number 1-16, the code would have to go through over 20 trillion permutations which could take hundreds of years to run.

I realized I would have to think a lot harder to create a more efficient solution for a problem of this size. This repository shows the code I wrote to create this more efficient solution using python and SQL.

At first I used the code in the folder 'first attempt'. These files of code put all the permutations of 4 numbers from 1 to 16 that add up to 34 without repeats into a database. Then it used those permutations to create squares whose edges add up to 34 and put those into the database as well. Then it tried to find 2 squares which would make a solution. However, this approach did not work. I realized that there was a mistake in the code written to create the squares and that I could also take a step out of this process.

In the folder 'second attempt' I have code which produces all the possible solutions to this problem. Here, I use almost exactly the same code to create the permutations of 4 numbers that add up to 34 and add them to a database. Then I use very similar code to create the squares, fixing the earlier mistake I had made. However, I do not add them to the database after creating them. Instead, I then look for the permutations of 4 numbers from the database which could be added to the square to create a solution, if there are any. If I find a solution, I add that to the database. 

I ended up with 1,792 solutions. The code to add these solutions to the database took about an hour to run after going through all 4,036,864 possible squares. This is obviously much better than 3 days, however, I am still working on optimizing the solution so that it can be even more efficient.

