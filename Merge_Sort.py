def merge_sort(arr):
    if len(arr)<=1:
        return arr
    
    l=merge_sort(arr[:len(arr)//2])
    r=merge_sort(arr[len(arr)//2:])
    
    return merge(l,r)

def merge(a,b):
    a_index=b_index=0
    c=[]
    while a_index<len(a) and b_index<len(b):
        c.append(min(a[a_index],b[b_index]))
        if a[a_index]<b[b_index]:
            a_index+=1 
        else:
            b_index+=1
        
    if a_index==len(a):
        c+=b[b_index:] 
    else:
        c+=a[a_index:]
    return c
