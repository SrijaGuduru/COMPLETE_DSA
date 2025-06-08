#day-4 afternoon
'''take any array and take k value ,use recursions to find subsets,
if subset sum is zero after iterations with k then subset is avaliale'''
#to check whether subset k sum exist or not
'''def subset(x,k,i):
    if k==0:
        return True
    if(i==0):
        return False
    if(x[i-1]>k):
        return subset(x,k,i-1)
    return subset(x,k-x[i-1],i-1) or subset(x,k,i-1)
a=[1,4,5,8]
k=9
print(subset(a,k,len(a)))'''



'''def subsets(x,k,s=[],i=0): 
    if (i==len(x)):
        if(k==0):
            print(s)
        return
    if (x[i]<=k):
        subsets(x,k-x[i],s+[x[i]],i+1)
    subsets(x,k,s,i+1)
a=[2,3,4,5]
k=9
subsets(a,k)'''



#testcase1
'''input:[2,4,6,8]
13
output:-1'''
#testcase2
'''input:[2,4,6,8]
14
output:2'''
'''def find_subset_sum_zero(arr, k, current=[], index=0):
    if len(current) == k:
        if sum(current) == 0:
            return True
        return False
    if index == len(arr):
        return False

    
    if find_subset_sum_zero(arr, k, current + [arr[index]], index + 1):
        return True
    
    if find_subset_sum_zero(arr, k, current, index + 1):
        return True

    return False

arr = list(map(int, input().split()))
k = int(input())


if find_subset_sum_zero(arr, k):
    print(-1)
else:
    print(min(arr))'''
    
    
    
    
    
#take list from user ,finf the largest even number and smallest odd number using greedy algorithm
'''a=[4,5,6,2,13,7,8]
m=0
m1=999999
for i in a:
    if(i>m and i%2==0):
        m=i
    if(i<m1 and i%2!=0):
        m1=i
print(m,m1)'''

#find the second largest number of a array
a=[4,5,6,8,2,4,13,7,4]
m=0
m1=0
for i in a:
    if(i>m):
        m=i-1
print(m)












