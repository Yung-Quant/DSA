#implementation of bubble sort, increasing order

def BBSort(array):
	for j in range(len(array)-1):
		for i in range(len(array)-1):
			if array[i] > array[i+1]:
				temp = array[i]
				array[i] = array[i+1]
				array[i+1] = temp
	return array

#driver
a = [1,2,3,4,5,6,7]
print(BBSort(a))