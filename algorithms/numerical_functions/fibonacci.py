from random import randint
import sys
from utilities.memoize import memoize

def fib0(n):
	return n if n < 2 else fib0(n-1) + fib0(n-2)

@memoize
def fib1(n):
	return n if n < 2 else fib1(n-1) + fib1(n-2)

