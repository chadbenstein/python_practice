#Let's say I give you a list saved in a variable:

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#Write one line of python that takes this list and makes it a new list that has only the even elements of this list in it

def even_list_numbers(list):
    return [num for num in a if num%2 == 0] # logic surrounded by brackets makes it a new list. Necessary to successfully return. Logic goes --> return iterable for itself in our list if iterable is divisible by 2


print even_list_numbers(a)
