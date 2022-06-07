import random

#A function that produces an list of the numbers 1-16 inclusive arranged in a random order
def getnums():
    nums = []
    i = 0
    while True:
        num = random.randint(1,16)
        if num not in nums:
            nums += [num]
            i += 1
        if i == 16:
            break
    return nums

arrlist = []
#A loop which uses the above function to get the randomly ordered list of numbers 1-16 and checks that the random order has not been seen before
#by storing each list that has been used in another list and checking that the list from the 'getnums' function is not in the list 'arrlist'.
#Each index in the list represents a position on the squares. The rest of the loop checks that the numbers along the edges of the squares add up to 34.
#If a solution is found the loop is stopped and the list is printed.
while True:
    while True:
        nums = getnums()
        if nums not in arrlist:
            arrlist += [nums]
            break
    sums = []
    sums += [sum(nums[0:4])]
    sums += [sum(nums[3:7])]
    sums += [sum(nums[6:10])]
    sums += [sum(nums[9:12]) + nums[0]]
    sums += [sum(nums[11:14]) + nums[1]]
    sums += [nums[15] + nums[13] + nums[2] + nums[4]]
    sums += [sum(nums[14:]) + nums[5] + nums[7]]
    sums += [nums[14] + nums[8] + nums[10] + nums[12]]
    if all(num == nums[0] for num in nums) and (nums[0] == 34):
        break
print(f"{nums}")
