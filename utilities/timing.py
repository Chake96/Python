import time

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
		time.time()
		if t-t0 > dt:
			break
	print(t-t0)
	return ((t-t0/k), result)

