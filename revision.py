"""
TEST SKELETON
Topics covered:
- Conditional statements
- Functions
- Basic loops
- Advanced loops
- Simple algorithms
"""

# ===============================
# SECTION 1 — CONDITIONALS
# ===============================

def check_number(num):
    """
    Determine whether a number is positive, negative, or zero.
    """

    # TODO:
    # if number > 0 → return "Positive"
    # if number < 0 → return "Negative"
    # otherwise → return "Zero"

    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"
print(check_number(2))
print(check_number(-1))
print(check_number(0))



def check_mark(mark):
    """
    Determine pass or fail based on mark.
    """

    # TODO:
    # if mark >= 50 → return "Pass"
    # else → return "Fail"

    if mark >= 50:
        return "Pass"
    else:
        return "Fail"
print(check_mark(55))
print(check_mark(45))


# ===============================
# SECTION 2 — BASIC LOOPS
# ===============================

def sum_to_n(n):
    """
    Return the sum of numbers from 1 to n.
    Example: n=4 → 1+2+3+4 = 10
    """

    # TODO:
    # create total variable = 0
    # loop from 1 to n
    # add each number to total
    # return total
    total = 0
    for i in range(1,n + 1):
        total += i
    return total
print(sum_to_n(5))


def count_even(numbers):
    """
    Count how many even numbers exist in a list.
    """

    # TODO:
    # create counter = 0
    # loop through numbers
    # if number % 2 == 0
    # increase counter
    # return counter
    total = 0
    for i in numbers:
        if i % 2 == 0:
            total += 1
    return total
print(count_even([1,2,3,4,6]))



# ===============================
# SECTION 3 — ADVANCED LOOPS
# ===============================

def find_max(numbers):
    """
    Find the largest number in a list.
    """

    # TODO:
    # assume first number is max
    # loop through list
    # if number > max
    # update max
    # return max

    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
print(find_max([3,7,2,9]))

def factorial(n):
    """
    Calculate factorial of n.
    Example: 5! = 120
    """

    # TODO:
    # start result = 1
    # loop from 1 to n
    # multiply result by each number
    # return result

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(factorial(5))



# ===============================
# SECTION 4 — SIMPLE ALGORITHMS
# ===============================

def reverse_list(items):
    """
    Reverse a list without using reverse().
    """

    # TODO:
    # create empty list
    # loop backwards through items
    # append each element
    # return reversed list

    
    reversed_items = []

    for i in range(len(items) - 1, -1, -1):
        reversed_items.append(items[i])

    return reversed_items

print(reverse_list(["1","2","3"]))
print(reverse_list([1,2,3]))


def find_duplicates(items):
    """
    Return duplicates in a list.
    """

    # TODO:
    # create seen set
    # create duplicates list
    # loop through items
    # if item already in seen → add to duplicates
    # else → add to seen
    # return duplicates

    seen = set()
    dup_items = []
    for i in items:
        if i in seen:
            if i not in dup_items:
                dup_items.append(i)
        else:
            seen.add(i)
    return dup_items

print(find_duplicates(["python", "code", "slindile", "python", "slindile"]))

