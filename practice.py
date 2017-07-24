
#Take a list, say for example this one:

a_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

#and write a program that prints out all the elements of that list that are less than 5.

#Extra Credit:
#1. Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
#2. Write this in one line of Python
#3. Ask the user for a number and return a list that contains only elements from the original list "a" that are smaller than that number given by the user.

# 1. Print elements < 5 in new list.

#def remove_add(list):
#    new_list = [] #make a new, empty list.
#    for i in a_list: #for loop allows us to loop through the entire list
#        if i < 5:
#            new_list.append(i) #script adds list item to new_list if it's less than 5
#    return new_list #return value to function

#print remove_add(a_list)

# 2. Same as above. Write in one line of code.

#def remove_add(list):
#    return [i for i in list if i<5] # Referenced codewars solutions. We don't need to create a new list locally, or globally. We can set the value of the function to be a list. Arguments are the same as they'd be in multiple lines.

#print remove_add(a_list)

# 3. Ask for user input, then have function return list of numbers that are less than user input.

#def remove_add(list):
#    hi_num = int(raw_input("Pick any number less than or equal to 100: ")) #asks user for number && converts response to integer value
#    return [i for i in list if i<hi_num] #single-line solution to return a list of numbers less than user's response. 

#print remove_add(a_list)


