import time
from datetime import datetime as dt

#timing ns, iterations, on a scale of dt seconds default 1min
def timeFunction(function, ns = 1000, dt = 60):
	t = t0 = time.time()
	for k in range(1, ns):
		function()
		t = time.time()
		if t-t0 > dt:
			break
	return (t-t0/k)

#returns time and result of function
def timeFunctionTupleReturn(function, ns = 1000, dt = 60):
	t = t0 = time.time()
	result = 0
	for k in range(1, ns):
		result = function()
		t = time.time()
		if t-t0 > dt:
			print(k)
			break
	return ((t-t0/k), result)

def time_func_tuple_return(function, num_iters = 1):
	result = 0
	if(num_iters < 1):
		raise Exception("number of iterations must be greater than or equal to 1")
	else:
		start = dt.now()
		for i in range(0, num_iters):
			result = function()
		end = dt.now()
		elapsed = end - start
	return result, elapsed
