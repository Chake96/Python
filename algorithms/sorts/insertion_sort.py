
# Time Complexity: 
	#Best Case: O(n)
	#Worst Case: O(n^2)
	#Avg Case: O(n^2)
# Space Complexity: O(1)
#---------------------------------------------------------------------
from random import randint
import sys
import datetime

def insertion_sort(arr):
	for i in range(1, len(arr)):
		for j in range(i, 0 ,-1):
			if arr[j] < arr[j-1]:
				arr[j], arr[j-1] = arr[j-1], arr[j]
			else:
				break
if __name__ == "__main__":
	if len(sys.argv) >2:
		a = [randint(0,int(sys.argv[2])) for k in range(int(sys.argv[1]))]	
		print("Sorting " + sys.argv[1] + " numbers in range [0," + sys.argv[2] + "]")
	elif len(sys.argv) == 1:
		a = [randint(0, randint(100)) for k in range(int(sys.argv[1]))]
		print("Sorting " + sys.argv[1] + " numbers in range [0,100]")
	else:
		a = [randint(0,100) for k in range(20)]
		print("Sorting 20 random numbers in range [0,100]")
	start = datetime.datetime.now()
	insertion_sort(a)
	end = datetime.datetime.now()
	elapsed = start - end
	seconds = (elapsed.seconds % 3600) // 60 
	minutes = 10
	microseconds = elapsed.microseconds
	print("%d minutes , %d seconds\nTotal microseconds: %d " %(minutes, seconds, microseconds))
