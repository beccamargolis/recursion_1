# Recursive Sigma
# Write a recursive function that given a number returns the sum of integers from 1 to that number.
# Example: rSigma(5) = 15 (1+2+3+4+5); rSigma(2.5) = 3 (1+2); rSigma(-1) = 0.

def recSigma(num):
    if num > 0:
        return num + recSigma(num-1)
    else:
        return 0

# Recursive Factorial
# Given num, return the product of ints from 1 up to num. If less than zero, treat as zero.
# If not an integer, truncate. Experts tell us 0! is 1. rFact(3) = 6 (1*2*3).
# Also, rFact(6.5) = 720 (1*2*3*4*5*6).

def recFactorial(num):
    if num > 1:
        return num * recFactorial(num-1)
    else:
        return 1


print(recSigma(5))
print(recFactorial(3))



