#Ask the user for a number. Depending on whether the number is odd or even, print out the appropriate message to the user. HINT: how does an even / odd number react differently when divided by 2?

#Extra Credit:
#1. If the number is a multiple of 4, print out a different message
#2. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
#def evenOdd(x):
#    n = float(raw_input("Pick a number. Any number: "))
#    number = str(n/2)
#    decimal_check = number[-2:]
#    if decimal_check == ".5":
#        print "The number is odd."
#    else:
#        print "The number is even."
#    print x
#evenOdd(2)

#def oddEven(random):
#    n = int(raw_input("Pick a number. Any number: "))
#    if n%2 == 1:
#        print "That number is odd"
#    else:
#        print "That number is even"
#    if n % random == 0:
#        print "Your number is divisible by " + str(random)
#oddEven(4)

#def checkNum(h):
#    num = int(raw_input("Pick a number. Any number: "))
#    check = int(raw_input("Pick another number. Any number: "))
#    if num % check == 0:
#        print str(check) + " divides evenly into " + str(num) + "!"
#    else:
#        print str(check) + " does not divide evenly into " + str(num) + " :("
