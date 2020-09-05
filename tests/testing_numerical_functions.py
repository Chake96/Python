from algorithms.numerical_functions import fibonacci
import utilities.timing as timing

if __name__ == "__main__":
	
	timea, a = timing.timeFunctionTupleReturn(lambda:fibonacci.fib0(20))
	timeb, b = timing.timeFunctionTupleReturn(lambda:fibonacci.fib1(20))
	print("Fibonacci without memoize took %10f seconds and got result: %d\nFibonacci with memoize took %0.0f seconds and got result:%d"%(timea, a,timeb, b))
	print(timing.timeFunction(lambda:fibonacci.fib0(5)))
