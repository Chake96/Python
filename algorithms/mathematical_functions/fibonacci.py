from random import randint
import sys
from ..utilities import memoize

def fib0(n):
	return n if n < 2 else fib(n-1) + fib(n-2)

@memoize
def fib1(n):
	return n if n < 2 else fib(n-1) + fib(n-2)


if __name__ == "__main__":
	if(len(sys.args)) < 1:
		print(fib1(1))
	else:	
		print(fib(sys.args[1]))
	
