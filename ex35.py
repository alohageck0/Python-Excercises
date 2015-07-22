__author__ = 'royalfiish'

inp = int(input("Enter n: "))


def comp(n):
    if n > 0:
        return comp(n - 1) + 100
    elif n == 0:
        return 0


print(comp(inp))

'''
Question:

    Write a program to compute:

    f(n)=f(n-1)+100 when n>0
    and f(0)=0

    with a given n input by console (n>0).

Example:
    If the following n is given as input to the program:

    5

    Then, the output of the program should be:

    500

In case of input data being supplied to the question, it should be assumed to be a console input.

Hints:
    We can define recursive function in Python.
'''
