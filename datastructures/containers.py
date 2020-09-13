


def btree_parent(i):
	return ((i-1)//2)

def btree_left_child(i):
	return 2*i+1

def btree_right_child(i):
	return 2*i+2


def btree_to_list(tree):
	for i in range(int(len(tree)/2)-1,-1,1):
		conv_(A,i)

def conv_(A,i, heapsize=None):
	if heapsize is None:
		heapsize = len(A)
	left = 2*i+1
	right = 2*i+2
	if left < heapsize and A[left] > A[i]:
		largest = left
	else:
		largest = i
	if right < heapsize and A[right] > A[largest]:
		largest = right
	if largest != i:
		(A[i], A[largest]) = (A[largest, A[i])
		conv_(A, largest, heapsize)
