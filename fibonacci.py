#Ask the user to enter a number
#This is the namount of numbers that will be generated in a fibonacci sequence.

def init_func():
    fibonacci_count = int(raw_input("How many fibonacci numbers would you like me to produce?: "))

    count = print_the_fib(fibonacci_count)

    print count

def print_the_fib(user_number):
    fibonacci = []
    index = 0
    while index < user_number:
        next_number = 0
        if index == 0:
            fibonacci.append(1)
            index += 1
        if index == 1:
            fibonacci.append(1)
            index += 1
        next_number = int(fibonacci[index-2]) + int(fibonacci[index-1])
        fibonacci.append(next_number)
        index += 1
    return fibonacci

init_func()
###
