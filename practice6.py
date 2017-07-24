#Ask the user for a string and print out whether this string is a palindrome or not. A palindrome is a string that reads the same forwards and backwards.)

#Extra Credit -- use %s within your string


#user_input = raw_input("Write something and I'll see if it's a palindrome: ")

#def palindrome(string):
#    if string[:] == string[::-1]:
#        print "Yes " + user_input + " is a palindrome."
#    else:
#        print "Nope " + user_input + " is not a palindrome."

#palindrome(user_input)


##   EXTRA   ##

user = raw_input("Write a word and I'll tell you if it's a palindrome: ")

def new_palindrome(string):
    if user==user[::-1]:
        print "Yes, %s is a palindrome" % (user)
    else:
        print "No, %s is not a palindrom" % (user)

new_palindrome(user)






## code here
