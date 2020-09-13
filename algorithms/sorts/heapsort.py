from datastructures.containers import *
def heapsort(A):
	btree_to_list(A)
	sz = len(A)
	for i in range(sz-1, 0, -1):
		A[0], A[i] = A[i], A[0]
		ds._conv(A,0, i)
