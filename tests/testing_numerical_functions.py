from algorithms.numerical_functions import fibonacci
import utilities.timing as timing

if __name__ == "__main__":
	a_result, a_time = timing.time_func_value_time(lambda:fibonacci.fib0(20), 10000)
	b_result, b_time = timing.time_func_value_time(lambda:fibonacci.fib1(20), 10000)
	print("Fibonacci without memoize took %10F seconds and got result: %d\nFibonacci with memoize took %f seconds and got result:%d"%(a_time.total_seconds(), a_result,b_time.total_seconds(), b_result))
