# //////////////////////////////////////
# Mis 1 : wrong order
# //////////////////////////////////
"""
def fizzbuzz(num):
    for i in range(1, num):
        if num % 3 == 0:
            print("Fizz")
        if num % 5 == 0:
            print("Buzz")
        if num % 3 == 0 & num % 5 == 0:
            print("FizzBuzz")
    return
"""
# /////////////////////////////////////////////////////////////////
#  Fix : Order = Hasses : FizzBuzz -> Fizz -> Buzz -> Success
# /////////////////////////////////////////////////////////////


"""

def fizzbuzz(num):
    for i in range(1, num):
        if num % 3 == 0 & num % 5 == 0:
            print("FizzBuzz")
            break

        if num % 3 == 0:
            print("Fizz")
            break

        if num % 5 == 0:
            print("Buzz")
            break

    return
"""

# ///////////////////////////////////////////////////////////////////////////////////
# Mis 2 : UnNeeded Code : 1. Removed break statements , 1. Added + 1 to num
# //////////////////////////////////////////////////////////////////////////

"""
def fizzbuzz1(num):
    for i in range(1, num + 1):
        if num % 3 == 0 & num % 5 == 0:
            print("FizzBuzz")

        if num % 3 == 0:
            print("Fizz")

        if num % 5 == 0:
            print("Buzz")

    return

"""
# fizzbuzz1(5)

# ///////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////
#  MIS 3 FUNDAMENTAL MIS : Used Num Instead of i In calculations.
# ////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////

"""
def fizzbuzz(num):
    for i in range(1, num + 1):
        if num % 3 == 0 & num % 5 == 0:
            print("FizzBuzz")
            continue

        if num % 3 == 0:
            print("Fizz")
            continue

        if num % 5 == 0:
            print("Buzz")
            continue

    return
"""

# ///////////////////////////////////////////////////////////////////////////////
#  MIS 4 FUNDAMENTAL MIS : Used & instead of Logical Operator "and".
# ////////////////////////////////////////////////////////////////////////////


def fizzbuzz(num):
    for i in range(1, num + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
            continue

        if i % 3 == 0:
            print("Fizz")
            continue

        if i % 5 == 0:
            print("Buzz")
            continue

    return

fizzbuzz(100)


