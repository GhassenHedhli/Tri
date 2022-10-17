from turtle import right


def sort_heatsort(l):
    n=len(l)
    for i in range( n // 2-1,-1,-1):
        restore_heap_properties(l,n,i)
    for i in range(n-1,0,-1):
        l[i],l[0]=l[0],l[i]
        restore_heap_properties(l,i,0)

def restore_heap_properties(l,n,i):
    maxVal=i
    left=2*i+1
    right=2*i+2
    if left<n and l[maxVal]<l[left]:
        maxVal=left

    if right<n and l[maxVal]<l[right]:
            maxVal=right
            
    if maxVal!= i:
        l[i],l[maxVal]=l[maxVal],l[i]
        restore_heap_properties(l,n,maxVal)

l=[11,39,9,2,8,87,92,63,74,6,5,69,63,33,46]
print(l)
sort_heatsort(l)
print(l)