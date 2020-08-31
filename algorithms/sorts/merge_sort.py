# A divide and conquer algorith
# Time Complexity:
#	Best Case: O(nlogn)
#	Worst Case: O(nlogn)
#	Avg Case: O(nlogn)
# Space Complexity: O(n)
# Single Function Implementation vs Function with Helper
	# helper function is the faster implementation 
#---------------------------------------------------------------
from random import randint
import sys
import datetime
#python3 single function sort1 implementation
def sort1(arr):
	if len(arr) > 1:
		mid = len(arr)//2
		left = arr[:mid]
		right = arr[mid:]
		sort1(left)
		sort1(right)
		i = j = k = 0

		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				arr[k] = left[i]
				i += 1
			else:
				arr[k] = right[j]
				j += 1
			k += 1
		while i < len(left):
			arr[k] = left[i]
			i+=1
			k+=1
		while j < len(right):
			arr[k] = right[j]
			j += 1
			k += 1
#merge sort with a helper function
def sort2(arr, l=0, r=None):
	if r is None: 
		r = len(arr)
	if l < r-1:
		mid = (l+r)//2
		sort2(arr, l,mid)
		sort2(arr, mid,r)
		merge(arr, l, mid, r)
#helper function to merge the arrays/lists from sort2
def merge(arr, l, mid, r):
	result, i, j = [], l, mid
	while True:
		if arr[i] <= arr[j]:
			result.append(arr[i])
			i += 1
		else:
			result.append(arr[j])
			j += 1
		if i == mid:
			while(j < r):
				result.append(arr[j])
				j+=1
			break
		if j == r:
			while(i < mid):
				result.append(arr[i])
				i+=1
			break;
	arr[l:r] = result

#non-recursive merge sort
def sort3(arr):
	blocksize, n = 1, len(arr)
	while blocksize < n:
		for p in range(0, n, 2*blocksize):
			q = p + blocksize
			r = min(q+blocksize, n)
			if r > q:
				merge(arr, p, q, r)
		blocksize = 2*blocksize

if __name__ == "__main__":
	if len(sys.argv) >2:
		a = [randint(0,int(sys.argv[2])) for k in range(int(sys.argv[1]))]
		print("Sorting " + sys.argv[1] + " numbers in range [0," + sys.argv[2] + "]")
	elif len(sys.argv) > 1:
		a = [randint(0, randint(100)) for k in range(int(sys.argv[1]))]
		print("Sorting " + sys.argv[1] + " numbers in range [0,100]")
	else:
		a = [randint(0,100) for k in range(20)]
		print("Sorting 20 random numbers in range [0,100]")
	start = datetime.datetime.now()
	b = a
	sort1(b)
	end = datetime.datetime.now()
	elapsed = end - start
	microseconds = elapsed.microseconds
	total_seconds = elapsed.total_seconds()
	minutes = (total_seconds //60)%60
	seconds = (total_seconds %60)
	print("Single Function Time elapsed(min:sec) = %d:%d \nTotal Seconds: %d \nTotal microseconds: %d " %(minutes, seconds, total_seconds, microseconds))
	start = datetime.datetime.now()
	c=a
	sort2(c)
	end = datetime.datetime.now()
	elapsed = end - start
	microseconds = elapsed.microseconds
	total_seconds = elapsed.total_seconds()
	minutes = (total_seconds //60)%60
	seconds = (total_seconds %60)
	print("Function with Helper Time elapsed(min:sec) = %d:%d \nTotal Seconds: %d \nTotal microseconds: %d " %(minutes, seconds, total_seconds, microseconds))
	start = datetime.datetime.now()
	sort3(a)
	end = datetime.datetime.now()
	elapsed = end - start
	microseconds = elapsed.microseconds
	total_seconds = elapsed.total_seconds()
	minutes = (total_seconds //60)%60
	seconds = (total_seconds %60)
	print("Non-Recursive Function with Helper Time elapsed(min:sec) = %d:%d \nTotal Seconds: %d \nTotal microseconds: %d " %(minutes, seconds, total_seconds, microseconds))















