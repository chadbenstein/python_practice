#Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)


#is 26 a divisor for itself? because 26 / 26 == 1
# need to loop through function and have raw_input%i every time.
#while i < raw_input?? (see point above)
# if raw_input%i == 0, append to new list.

def divisor_check():
    divisee = int(raw_input("Pick any number. Any! And I'll tell you what numbers divide evenly into it: ")) #variable to store user request
    new_list = []
    #i = 1
    #while i <= divisee:
    #    if divisee%i == 0:
    #        new_list.append(i)
    #    i += 1
    #return new_list

    



print divisor_check()


#your code here
