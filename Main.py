# Python Challenges
import math

#  1) The Time Stone: Lets get cosmic here and begin working with Time.

# - First, lets create a function that converts Minutes to Seconds (1 ->60, 5 -> 300)
# -  Then take it up a step further, converting Hours into seconds (1 -> 3600)
# -  We're on the right track here, how many seconds are in a day
# - How many Hours are in the month of June? 
# - How many Minutes are in the month of August?
 
 # Bonus -> Without singing the old showtune in your head, how many Minutes are there in a year?
#In days, in weeks, in cups of coffee?

def minutes_to_seconds():
    minutes = 1
    seconds_in_a_minute = 60
    min_in_secs = minutes * seconds_in_a_minute

    print(min_in_secs)

minutes_to_seconds()

def hours_to_seconds():
    hour = 1
    seconds_in_hour = 3600
    hour_in_secs = hour * seconds_in_hour

    print(hour_in_secs)

hours_to_seconds()

def seconds_in_day():
    seconds_in_hour = 3600
    hours_in_day = 24
    seconds_day = seconds_in_hour * hours_in_day

    print(seconds_day)

seconds_in_day()

def hours_in_june():
    hours_in_day = 24
    days_in_june = 30
    june_seconds = (days_in_june * hours_in_day)

    print(june_seconds)

hours_in_june()

def minutes_in_august():
    minutes_in_hour = 60
    days_in_august = 31
    hours_in_day = 24
    minutes_august = hours_in_day * days_in_august * minutes_in_hour
    
    print(minutes_august)

minutes_in_august()
    
def minutes_in_year():
    minutes_in_day = 24 * 60
    days_in_year = 365
    minutes_in_year = minutes_in_day * days_in_year
    print(minutes_in_year)

minutes_in_year()

def minutes_in_day():
    minutes_in_hour = 60
    hours_in_day = 24
    mins_in_day = minutes_in_hour * hours_in_day
    print(mins_in_day)

minutes_in_day()

def minutes_in_week():
    minutes_in_hour = 60
    hours_in_day = 24
    days_in_week = 7
    mins_in_week = hours_in_day * days_in_week * minutes_in_hour
    print(mins_in_week)

minutes_in_week()


#  2) Middle letter
# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.
# For example, mid("abc") should return "b" and mid("aaaa") should return "".

def mid(str):
    word_length = len(str)
    print(word_length)
    if word_length % 2 == 0:
        return ''
    else:
        mid_letter = int((word_length -1) / 2)
        middle_letter = str[mid_letter]
        return(middle_letter)

print(mid('cater'))

# ### 3) Hide the credit card number
# Write a function in Python that accepts a credit card number. It should return a string where all the characters are hidden with an asterisk except the last four. For example, if the function gets sent "1234567894444", then it should return "*********4444".

def hidden():
    credit_card = '1234567894444'
    hidden_nums = '*' * (len(credit_card) - 4) + credit_card[ - 4: ]
    print(hidden_nums)

hidden()


# ### 4) Online status
# The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.
# For example, consider the following dictionary:

statuses = {
    "John": "online",
    "Paul": "offline",
    "George": "online",
    "Ringo": "offline"
}


# In this case, the number of people online is 2.
# Write a function named online_count that takes one parameter. The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above.
# Your function should return the number of people who are online.


##would only want to use if you were referencing statuses dictionary
def online_count():
    statuses_values = [statuses[key] for key in statuses]
    print(statuses_values.count('online'))
online_count()

##can use multiple times with different dictionaries
def online_count(dictionary):
    dictionary_values = [dictionary[key] for key in statuses]
    print(dictionary_values.count('online'))   

online_count(statuses)

#  5) Give me the discount
# Create a function in Python that accepts two parameters. The first should be the full price of an item as an integer. The second should be the discount percentage as an integer.
# The function should return the price of the item after the discount has been applied. For example, if the price is 100 and the discount is 20, the function should return 80.

def show_discount(price , discount_percentage):
    discount = (discount_percentage / 100) * price
    return (price - discount)

print(show_discount(100, 20))


#  6) Pythagorean Theorum
# As any High School sophomore will tell you, the sum of the squares of two legs of a right trangle will equal the square of the hypotenuse.
# Create a function that takes two integers as the Adjacent and Opposite legs of a triangle, and returns an integer of the Hypotenuse

def get_hypotenuse():
    a = 3
    b = 4

    hypotenuse = math.sqrt(a**2 + b**2)
    print(hypotenuse)

get_hypotenuse()

def get_hypotenuse(a, b):
    return int((a**2 + b**2)** 0.5)

print(get_hypotenuse(3, 4))


#  7) Fibonacci Sequence 
# Everyone's favorite Math Problem!
# The Fibonacci numbers are the numbers in the following integer sequence.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
# In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation between two adjacent steps in a list
# Create a python function that takes two numbers and finds the next Nine intervals using the Fibonacci Sequence

def fib_seq(): #fib sequence using while
    n= 9
    num1 = 0
    num2 = 1
    next_number = num2
    count = 1

    while count <= n:
        print(next_number, end= '')
        count +=1
        num1, num2 = num2, next_number
        next_number = num1 +num2

print(fib_seq())

def fibonacci(num1, num2, count):
    sequence = [num1, num2]
    for x in range(count):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence
print(fibonacci(0, 1, 9))