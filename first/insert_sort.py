lst = [49,38,65,97,76,13,27,49] 
def insert_sort(lists):   
    for i in range(1,len(lists)) :  
        j = i-1  
        key = lists[i]  
        while j >= 0:  
            if key < lists[j]:  
                lists[j+1]=lists[j]  
                lists[j]=key  
            j=j-1  
    return lists   

