# ////////////////////////////////////////////////////////////////////////////////
#                                   REMASTERED PYTHON
# //////////////////////////////////////////////////////////////////////////
"""
Challenge 1: FizzBuzz (Classic)
Print numbers 1 to 100, but:

Multiples of 3 → print "Fizz"

Multiples of 5 → print "Buzz"

Multiples of both → print "FizzBuzz"

python
"""
# //////////////////////////////////////////////////////////////////////////////
#                                     Design
# ///////////////////////////////////////////////////////////////////////

"""

#  DESIGN
#       Old Design :
#           If divisable by 3 print fizz , divisibe by 5 print buzz ,
#           if divisable by both print fizz buzz


#  MASTERY
#       New Design : 
#           Anything Improve able?
#               Improvements :
#               -   mastery on lang by writing in one line. 
#               -   Writing speed by Typing more.
#               -   understandings by writing hard challenge.
#               Deeds :
#               -   solve this quetion a 100 times.
#               -   Everytime a diffrent way.


"""


# ////////////////////////////////
#  1st way : Old way
# //////////////////////////

# ////////////////////////////////////////////////////////////
# Hasses's Dia: function -> 3 if elses -> Print statements
# Notes : F capital, FizzBuzz = No spaces and b capital
# ///////////////////////////////////////////////////////

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

# //////////////////////////////////
#  2nd way : Language Mastery
# /////////////////////////////
# /////////////////////////////////////
#     Goal : Single line mastery
# /////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////////////
# Notes
"""
        What is a Lambda Function?
        :-   A lambda function is a small, anonymous function in Python that:

            Can have any number of arguments but only one expression

            Returns the result of that expression automatically

            Defined using the keyword lambda

            Often used for short, throwaway functions

        Syntax: lambda arguments: expression
"""

"""     
        Example:
                1.(lambda x: x > 2)(3) → True


                2.# Addition
                    (lambda a, b: a + b)(3, 5)  # 8

                    # Division with default
                    (lambda x, y=10: x / y)(20)  # 2.0


                3. # Sorting by second element  
                    pairs = [(1, 'z'), (2, 'a'), (3, 'm')]
                    sorted(pairs, key=lambda x: x[1])  # [(2, 'a'), (3, 'm'), (1, 'z')]

                    # Filtering
                    list(filter(lambda x: x > 2, [1, 2, 3, 4, 5]))  # [3, 4, 5]

                    # Mapping
                    list(map(lambda x: x * 2, [1, 2, 3, 4]))  # [2, 4, 6, 8]
                    
"""
"""
            Note :
                    Mistake Fixes : 
                            1. works only if placed under brackets
                            2. Spelled : "lambda"

"""
# ////////////////////////////////////////////////////////////////////////////////////////


# //////////////////////////////////////////////////////////////////////////////////
#  Hasses's 2nd way : funtion -> lambda condions * 3 -> Fizz , Buzz , FizzBuzz
# /////////////////////////////////////////////////////////////////////////////

#  INCOMPLETE
def FizzBuzz_1(num):
    fizzbuzz = []
    for i in range(num):
        (lambda x, y=3: x % y == 0)(print("Fizz"))
        (lambda x, y=5: x % y == 0)(print("Buzz"))
        (lambda x, y=5, z=3: x % y == 0 & x % z == 0)(print("FizzBuzz"))
    return
