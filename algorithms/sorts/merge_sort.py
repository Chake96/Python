# Time Complexity:
#Best Case: O(nlogn)
#Worst Case: O(nlogn)
#Avg Case: O(nlogn)
# Space Complexity: O(n)
#---------------------------------------------------------------
from random import randint
import sys
import datetime

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
	merge_sort(a)
	end = datetime.datetime.now()
	elapsed = end - start
	microseconds = elapsed.microseconds
	total_seconds = elapsed.total_seconds()
	minutes = (total_seconds //60)%60
	seconds = (total_seconds %60)
	print("Time elapsed(min:sec) = %d:%d \nTotal Seconds: %d \nTotal microseconds: %d " %(minutes, seconds, total_seconds, microseconds))
	if len(a) > 10000:
		print(a[-5:])
