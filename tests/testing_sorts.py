from algorithms.sorts import merge_sort
from algorithms.sorts import quick_sort
import utilities.timing as timing
from random import randint

if __name__ == "__main__":
	original = [randint(0, 1000) for k in range(1000)]
	merge_arr = original
	_, merge_sort3t = timing.time_func_tuple_return(lambda:merge_sort.sort3(merge_arr),10000)
	_, merge_sort2t = timing.time_func_tuple_return(lambda:merge_sort.sort2(merge_arr),10000)
	_, merge_sort1t = timing.time_func_tuple_return(lambda:merge_sort.sort1(merge_arr), 10000)
	print("Merge 3 Seconds %f\nMerge 2 Seconds %f\nMerge 1 Seconds %f"%(merge_sort3t.total_seconds(), merge_sort2t.total_seconds(), merge_sort1t.total_seconds()))
	quick_arr = original
	_, quick1t = timing.time_func_tuple_return(lambda:quick_sort.sort0(quick_arr), 10000) 
	_, quick2t = timing.time_func_tuple_return(lambda:quick_sort.sort1(quick_arr), 10000)
	print("Quick 2 Seconds %f\nQuick 1 Seconds %f"%(quick2t.total_seconds(),quick1t.total_seconds()))

