# implementation of selection sort

def selectionSort(array):

	for i in range(0,len(array)-1):
		indexMin = i

		for j in range(i+1,len(array)):
			if array[j] < array[indexMin]:
				indexMin = j
		if indexMin != i:
			temp = array[indexMin]
			array[indexMin] = array[i]
			array[i] = temp
	return array

#driver
a = [1,5,2,70,13,4]
print(selectionSort(a))