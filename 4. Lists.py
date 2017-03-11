from functools import reduce
import numpy as np

# 1.Write a function that takes a list of floats and integers and returns the sum.

# Solution: We can use the sum function.
def tall(numbers):
    # Check if the instance contain list
    if isinstance(numbers, list):
        return sum(list(numbers))
    else:
        return sum(numbers)

# Test sets A for experimental purpose as a function created above
numbers = [1, 2, 3, 4, 5, 0.2]
numsum = sum(list(numbers))
rtall = (1, 2, 3)
print("TEST A:")
print(sum(rtall))
print(numsum)

# Function call tall()
print("FINALLY! The real thing: ")
print(tall(numbers))


###########################################################################################################################################################

# 2.Write another function that returns the mean value.
def average(numbers):
    # Check if the instance contain list
    if isinstance(numbers, list):
        return sum(numbers) / len(numbers)
    else:
        return sum(numbers) / len(sum(numbers))

print("Another Function....! ")
print(average(numbers))

# Test sets B for experimental purpose
print("TEST B: More incoming tests!")
print(reduce(lambda x, y: x + y, numbers) / len(numbers))
print(sum(numbers) / len(numbers))

# 3.Install numpy and use it to calculate the sum and mean of a list.
print("Find Sum using Numpy: " + str(np.sum(numbers)))
print("Find Mean using Numpy: " + str((np.sum(numbers) / len(numbers))))

###########################################################################################################################################################

# 4.Try these steps:

spam = ['1', '3', '2', '4', '0', 'Steve', 'Alice', 'Bob']
B = spam
B.append('Something')
print(spam)
print(B)

# You will notice that changing B changes spam.
# Now try:

B = [] * 10
print(spam)
print(B)

# This does not change spam-Why?
# ANSWER: Because Spam and B are two different/individual objects.
# What happened at the beginning was B replicated list of contents from Spam.
# And any other changes afterwards will not effect each other.

###########################################################################################################################################################

# The zip function joins two lists. In Python 3, you can use it as list(zip(x,y)) where x and y are lists.
# This function works even if len(x) is not equal to len(y). It simply uses the shortest list.
# Write a function that works like zip but instead of taking the first elements it takes user defined elements.
# For example you might have a list x=[1, 2, 3] and y=[7,3,8,1,6,9,10] so instead of combining [(1,7),(2,3),(3,8)]
# You might want to combine the first element with the fourth and the third with the second and so on.


# Suggested solution: Zip function in reverse order

def custom_zip(x, y):
    zipper = []
    for i in reversed(range(len(x))):
        zipper.append((x[i], y[i]))
    return zipper

# Defining x and y
x = [1, 2, 3, 4, 5]
y = ['red','green','blue','yellow','brown']

# Function call, tests
print("Here comes a little bit different zip() function: e.g. reversed order")
print(custom_zip(x, y))

###########################################################################################################################################################

# Read the python files that I have uploaded to learn more about lists. Specifically,
# I would like you to read the do and do not with lists file. Uncomment the line
# C.insert(0,j*j) and comment C.append(j*j).
# You will notice that the program takes a long time to finish (remember Ctrl+C stops the program).
# I want you to think of the reason and why append doesn’t take much time.

# ANSWER:
#