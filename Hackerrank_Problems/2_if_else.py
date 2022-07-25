"""
Given an integer, n perform the following conditional actions:
    * If n is odd, print weird
    * If n is even and in the inclusive range of 2 to 5, print Not Weird
    * If n is even and in the inclusive range of 6 to 20, print Weird
    * If n is even and greater than 20, print Not Weird

Input: 
    * A single line containing a positive integer, n

Constrains:
    * 1 <= n <= 100
"""

positive_integer = int(input())

if positive_integer % 2 != 0:
    print("Weird")
if positive_integer % 2 == 0:
    if positive_integer in range(2, 6):
        print("Not Weird")
    if positive_integer in range(6, 21):
        print("Weird")
    if positive_integer >= 20:
        print("Not Weird")

"""
Question: When to use if, elif and else?
"""