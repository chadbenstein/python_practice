#Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

# EXTRA CREDIT - use the "range" function

#is 26 a divisor for itself? because 26 / 26 == 1
# need to loop through function and have raw_input%i every time.
#while i < raw_input?? (see point above)
# if raw_input%i == 0, append to new list.

def divisor_check():
    divisee = int(raw_input("Pick any number. Any! And I'll tell you what numbers divide evenly into it: ")) #variable to store user request
    new_list = []
    i = 1 #start count at 1. can't divide by 0
    while i <= divisee: #keep dividing by i for all values less than user input
        if divisee%i == 0:
            new_list.append(i) #only return values that are perfectly divisible
        i += 1 #increase the index by one, test again
    return new_list

print divisor_check()


# Extra Credit

def div_check():
    user_number = int(raw_input("Pick a number. I'll tell you all divisors for it: ")) #variable to store user request
    divisor_list = [] #empty list to send values
    
    for i in range(1, user_number+1): #start range at 1 because math cannot divide by 0. Add 1 to second argument to include the input from user as it divides into itself
        if user_number%i==0: #if there is no remainder
            divisor_list.append(i) #add that number to our empty list
    return divisor_list #set definition value to this list

print div_check()

#your code here
