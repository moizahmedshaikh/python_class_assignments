"""
Write a Python program to draw a pyramid of "*" using loops and string repetition...
"""

def pyramid_pattern():
    num = 5
    for i in range(1, num+1):
        print(" " * (num - i) + "*" * (2 * i-1))

pyramid_pattern()
