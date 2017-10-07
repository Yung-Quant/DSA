#implentation of insertion sort

def insertionSort(array):
	for i in range(1,len(array)):
		val = array[i]
		pos = i

		while pos > 0 and array[pos-1] > val:
			array[pos] = array[pos-1]
			pos = pos - 1
		if pos != i:
			array[pos] = val
	return array

#driver
a = [2,5,1,20,7,4]
print(insertionSort(a))