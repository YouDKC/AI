def bubble_sort(lst):
	for i in range(len(lst)):
		found = False
		for j in range(1,len(lst)-1):
			if lst[j-1] > lst[j]:
				lst[j-1],lst[j] = lst[j],lst[j-1]
				found = True
		if not found:
			break
