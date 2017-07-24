#Take two lists, say for example these two:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

#Extras:

#Randomly generate two lists to test this
#Write this in one line of Python

def list_overlap(a_list, b_list):
    new_list = []
    for number in a_list and b_list:
        if number in a_list and b_list:
            new_list.append(number)
    return new_list

#print list_overlap(a, b)


# Extras 1 -- randomly generate two lists to test this

import random

alist = random.sample(range(1, 10), 4) #creates a list of 4 random numbers, numbers range from 1-10
alist.sort() #sorts the list to arrange itself in ascending order

blist = random.sample(range(1, 10), 4)
blist.sort()

clist = [] #empty list for our function to store values

def list_check(x,y):
    for number in x and y: #for-loop that loops through both inputs
        if number in x and y:
            clist.append(number) #adds loop value to empty list if list item in both lists
    return clist #gives function value of our list

print alist
print blist #print both of these lists to manually check computation

print list_check(alist, blist)

#code goes here
