lst = [49,38,65,97,76,13,27,49] 
def select_sort(lst):
	for i in range(len(lst)-1):
		k = i 
		for j in range(i,len(lst)):
			if lst[j] < lst[k]:
				k = j
		if i != k:
			lst[i],lst[k] = lst[k],lst[i]
select_sort(lst)