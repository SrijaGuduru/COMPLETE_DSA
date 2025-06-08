#day4
#given array ,print frequency(k) value of an array without loops

'''array=[2,4,6,3,3,2,6,1,2,3,6,6,5]
k=6
print(array.count(k))'''


#second method using recursion
'''def frequency(arr,k):
    if not arr:
        return 0
    return (arr[0] == k) + frequency(arr[1:], k)
arr=[2,4,6,3,3,2,6,1,2,3,6,6,5]
k=6
print(frequency(arr,k))'''

#if given frequency value print that number
#one code
'''def frequency(arr,k):
    if not arr:
        return 0
    return (arr[0] == k) + frequency(arr[1:], k)
def unique_element(arr):
    if not arr:
        return []
    head=arr[0]
    rest=unique_element([x for x in arr[1:] if x != head])
    return [head]+rest
def element_with_frequency(arr,f):
    unique=unique_element(arr)
    if not unique:
        return
    if frequency(arr,unique[0]==f):
        print(unique[0])
    element_with_frequency(arr,f)
arr=[2,4,6,3,3,2,6,1,2,3,6,6,5]
f=4
print(element_with_frequency(arr,f))  '''



#second method
'''def  freq(a,x,i,c):
    if(i==len(a)):
        return c
    if(a[i]==x):
       return freq(a,x,i+1,c+1)
    return freq(a,x,i+1,c)
    
        
a=[2,4,6,3,3,2,6,1,2,3,6,6,5]
x=3
print(freq(a,x,0,0))'''



#print subsets using recursion
'''def print_subsets(arr,current=[],i=0):
    if i==len(arr):
        print(current)
        return
    print_subsets(arr,current+[arr[i]],i+1)
    print_subsets(arr,current,i+1)
a=input()
arr=list(map(int,a.strip().split()))
print(print_subsets(arr))'''



'''take any array and take k value ,use recursions to find subsets,
if subset sum is zero after iterations with k then subsetis avaliale'''
#to check whether subset k sum exist or not
def sub_set(x,k,i=0):
    if(i==len(x)):
        return False
    if(k==0):
        return True
    if(x[i]>k):
        return sub_set(x,k,i+1)
    return sub_set(x,k-x[i],i+1)
    

    
        



