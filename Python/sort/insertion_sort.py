array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def ins_sort(array):
	for i in range(1, len(array)):
		for j in range(i, 0, -1):
			if array[j - 1] > array[j]:
				array[j - 1], array[j] = array[j], array[j - 1]
			else:
				break

	return array
