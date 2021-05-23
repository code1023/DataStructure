def quick_sort(a):
	if len(a) < 2:
		return a
	
	pivot = a[len(a) // 2]
	low_a, equal_a, high_a = [], [], []

	for n in a:
		if n < pivot:
			low_a.append(n)
		elif n > pivot:
			high_a.append(n)
		else:
			equal_a.append(n)

	return quick_sort(low_a)+ equal_a + quick_sort(high_a)


d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
print(quick_sort(d)
