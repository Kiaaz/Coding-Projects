#declare an empty list
A=[]
#declare a list that has 10 zero elements:
A=[0]*10
#Make a list from any string
A=list('hello 1 02241212120')
print(A)
#And get it back
#''.join(A)
#Notice that you can sort this list
#Unlike what the book chapter says
A.sort()
print(A)
#But you cannot sort this:
spam = [1, 3, 2, 4, 'Alice', 'Bob']
#because the elements are different
#But you can sort this
spam = ['1', '3', '2', '4', 'Alice', 'Bob']
colors =['red','green','blue','yellow','brown']

for color in colors:
	print (color)

print ('lets do it in reverse order')

#print the list in reverse order
for color in reversed (colors):
	print (color)
#We can also reverse a list by:

colors.sort(reverse=True)
for color in colors:
	print (color)

print(enumerate (colors))
# returns an address to the list.

#print the elements of the list with their index.
for i, color in enumerate(colors):
	print (i, '-->', colors[i])

#What happens if we have two lists?

names=['Amanda','Mads','Peter','James','Suzan']
age=[4,52,40,27,70]

for name,your_age in zip(names,age):
	print (name,'-->', your_age)

for color in sorted(colors):
	print (color)

names_2=['Amanda','Mads','Peter','James','Suzan']
for name in sorted(names, reverse=True):
	print (name)

D=dict(zip(names,age))
print(D)

print(hex(id(D)))
print(id(names))
