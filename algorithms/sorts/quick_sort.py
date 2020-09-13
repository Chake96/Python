# A divide and conquer algorithm
# Time Complexity:
# 	Best Case: O(nlog(n))
#	Average: O(nlog(n))
#	Worst: O(n^2)
from random import randint

def partition(A, i ,j):
	x= A[i]
	h = i
	for k in range(i+1,j):
		if A[k] < x:
			h=h+1
			A[h], A[k] = A[k], A[h]
	A[h], A[i] = A[i], A[h]
	return h

def sort0(A, p = 0, r =-1):
	if r is -1:
		r = len(A)
	if p < r -1:
		q = partition(A, p, r)
		sort0(A,p,q)
		sort0(A,q+1,r)

#randomized quick sort
def sort1(A, p = 0, r = -1):
	if r is -1:
		r = len(A)
	if p < r -1:
		q = randint(p, r-1)
		A[p], A[q] = A[q], A[p]
		q = partition(A, p, r)
		sort1(A, p, q-1)
		sort1(A, q+1, r)
