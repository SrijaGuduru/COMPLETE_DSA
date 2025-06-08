#day_8
#binary search
'''ip:38
find the square root of number,answer should in floor value,no decimal value.don't use squareroot keyword,instead use binary search
'''
'''
def square_rt(num):
    if num<2:
        return num
    low=1
    high=num
    ans=1
    while low<=high:
        mid=(low+high)//2
        if mid*mid==num:
            return mid
        elif mid*mid<num:
            ans=mid
            low=mid+1
        else:
            high=mid-1
    return ans
a=38
print(square_rt(a))
'''



#second classmethod
'''
def square_root(n):
    l=0
    r=n//2
    while l<=r:
        m=(l+r)//2
        if m*m == n:
            return m
        elif m*m>n:
            r=m-1
        else:
            l=m+1
    return r
n=38
print(square_root(n))
'''


#[15,18,20,22,2,5,8,10,12,13]
#find where is the junction point,how many rotation happend
'''
def find_rotation_count(arr):
    low = 0
    high = len(arr) - 1

    while low <= high:
        if arr[low] <= arr[high]:
            return low  

        mid = (low + high) // 2
        next_idx = (mid + 1) % len(arr)
        prev_idx = (mid - 1 + len(arr)) % len(arr)

        if arr[mid] <= arr[next_idx] and arr[mid] <= arr[prev_idx]:
            return mid  

        if arr[mid] >= arr[low]:
            low = mid + 1
        else:
            high = mid - 1

    return 0


arr = [15, 18, 20, 22, 2, 5, 8, 10, 12, 13]
rotation_count = find_rotation_count(arr)
print(rotation_count)
print(arr[rotation_count])
'''


#another method
'''
def rotated_binary_serach(arr):
    l=0
    r=len(arr)-1
    while l<=r:
        m=(l+r)//2
        if arr[l]>arr[m]:
            r=m-1
        else:
            l=m+1
    return r,l
        
arr=[15,18,20,22,2,5,8,10,12,13]
print(rotated_binary_serach(arr))
'''
'''
a=[2,3,4,6,3,2,1,5,8,10,1,4,2]
l=0
r=len(a)-1
while(l<r):
    m=(l+r)//2
    if(a[m]>a[r]):
        l=m+1
    else:
        r=m
print(a[l],a[r])    
'''



#print the peak element
#ip:[2,3,4,6,3,2,1,5,8,10,1,4,2]
#peak eklement before elememt should greater and next elememt should lesser
'''
a=[2,3,4,6,3,2,1,5,8,10,1,4,2]
l=0
r=len(a)-1
while(l<r):
    m=(l+r)//2
    if(m==0 or a[m]>a[m-1] and m==len(a)-1 or a[m]>a[m+1]):
        print(a[m])
        break
    if(a[m+1]>a[m]):
        l=m+1
    else:
        r=m-1
'''



#875. Koko Eating Bananas
a=[3,6,7,11]
h=0
k=3
s=0
for i in a:
    s=s+math.cell(i/k)
    if(s>h):
        print("not")
        break
    else:
        print("possible")


    
    
    