# A divide and conquer algorithm
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
#python3 single function merge_sort implementation
def merge_sort(arr):
	if len(arr) > 1:
		mid = len(arr)//2
		left = arr[:mid]
		right = arr[mid:]
		merge_sort(left)
		merge_sort(right)
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
def merge_sort2(arr, l=0, r=None):
	if r is None: 
		r = len(arr)
	if l < r-1:
		mid = (l+r)//2
		merge_sort2(arr, l,mid)
		merge_sort2(arr, mid,r)
		merge(arr, l, mid, r)
#helper function to merge the arrays/lists from merge_sort2
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
	merge_sort(b)
	end = datetime.datetime.now()
	elapsed = end - start
	microseconds = elapsed.microseconds
	total_seconds = elapsed.total_seconds()
	minutes = (total_seconds //60)%60
	seconds = (total_seconds %60)
	print("Single Function Time elapsed(min:sec) = %d:%d \nTotal Seconds: %d \nTotal microseconds: %d " %(minutes, seconds, total_seconds, microseconds))
	start = datetime.datetime.now()
	merge_sort2(a)
	end = datetime.datetime.now()
	elapsed = end - start
	microseconds = elapsed.microseconds
	total_seconds = elapsed.total_seconds()
	minutes = (total_seconds //60)%60
	seconds = (total_seconds %60)
	print("Function with Helper Time elapsed(min:sec) = %d:%d \nTotal Seconds: %d \nTotal microseconds: %d " %(minutes, seconds, total_seconds, microseconds))
