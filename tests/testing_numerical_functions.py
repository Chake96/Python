from algorithms.numerical_functions import fibonacci


if __name__ == "__main__":
	a = fibonacci.fib0(20)
	b = fibonacci.fib1(10)
	print(a)
	print(b)
	#print("Fibonacci without memoize: %d\nFibonacci with memoize %d")%(a, b)
