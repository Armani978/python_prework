# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function

def hello_name(user_name):
    print("hello_" + user_name + "!")

hello_name("USERNAME")

# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds(x = 0):
    while x < 100:
        x += 1 
        if x % 2 == 0:
            continue

        print(x)
    


first_odds()

# Question 3
#Please write a Python function, max_num_in_list to return the max number of a given list

def max_num_in_list(a_list):
    a_list = [5, 2, 8, 10, 4]
    max_num = (max(a_list))
    print(max_num)

max_num_in_list('num')

# question 4
# Write a function to return if the given year is a leap year
def is_leap_year(a_year):
    if (a_year % 4) == 0:
        return True
    else:
        return False

    if (a_year % 100) == 0:
        return True
    else:
        return False
    if (a_year % 400) == 0:
        return True
    else:
        return False
   
# Driver Code
a_year = int(input("Year"))
if (is_leap_year(a_year)):
    print("is a leap year.")
else:
    print("is not a leap year")

# question 5 
# Write a function to check to see if all numbers in the list are consecutive numbers
def is_consecutive(a_list):
    a_list = [1, 2, 3, 4, 5]
    if a_list == sorted(a_list):
        return True
    else:
        return False

