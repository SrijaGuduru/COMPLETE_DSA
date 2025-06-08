#dAY-6
'''given an unsorted array sort them using bubble sort,but don't use dot method'''
'''input_str=input()
arr=list(map(int,input_str.split()))
n=len(arr)
for i in range(n):
    for j in range(0,n-i-1):
        if(arr[j]>arr[j+1]):
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
print(arr)'''


#second method
'''
a=[3,5,2,1,4,7,9,3]
c=0
for j in range(len(a)-1):
    f=False
    for i in range(len(a)-1-j):
        c=c+1
        if(a[i]>a[i+1]):
            f=True
            a[i],a[i+1]=a[i+1],a[i]
    if(f==False):
        break
    print(a)        
print(c)
'''



'''input;[5,2,3,8,1,6,7]
k=2
first two elements and last two elements should be sorted but middle elements should be sorted'''
'''
def sort_k(arr,k):
    start = k
    end= len(arr)-k
    for i in range(start,end):
        for j in range(i+1,end):
            if arr[j]<arr[i]:
                arr[j],arr[i] = arr[i],arr[j]
    return arr
arr=[5,2,3,8,1,6,7]
k=2
print(sort_k(arr,k))
'''



'''input:a[2,5,8,6,3,1,9,4,7]
k=4
print kth largest element'''
'''

def bubble_sort_desc(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:  
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  

def kth_largest_bubble(arr, k):
    bubble_sort_desc(arr)
    return arr[k - 1]  


a = [2, 5, 8, 6, 3, 1, 9, 4, 7]
k = 4
print(kth_largest_bubble(a, k))

'''



'''input:['c','e','a','b','f']
output:[a,b,c,e,f]
depending on ascii value sort them in ascending order'''
'''
arr=['c','e','a','b','f']
arr.sort(key=ord)
print(arr)
'''


'''intput:[[2,3],[5,1],[1,4],[2,7],[1,3]]
output:[[5,1],[2,3],[1,2],[1,4],[2,7]]
depending on secound value of subarray sort them in ascending order'''
'''
a=[[2,8],[5,1],[1,3],[7,2]]
for j in range(len(a)-1):
    f=True
    for i in range(len(a)-1-j):
        if(a[i][1]>a[i+1][1]):
            f=True
            a[i], a[i + 1] = a[i + 1], a[i]
    if(f==False):
        break
print(a)    
'''



'''ip:["zebra","cet","apple","cat"]
if first letter is same don't swap but if second letter is lesser or greater then swap'''

'''
def custom_sort(arr):
    n=len(arr)
    for i in range(n):
        swapped=False
        for j in range(n-i-1):
            s1,s2=arr[j],arr[j+1]
            if s1[0]>s2[0]:
                arr[j],arr[j+1]=s2,s1
                swapped=True
            elif s1[0]==s2[0]:
                if len(s1)>1 and len(s2)>1 and s1[1]>s2[1]:
                    arr[j], arr[j + 1] = s2, s1
                    swapped = True
                    
        if not swapped:
            break
    return arr
arr=["zebra", "cet", "apple", "cat"]
custom_sort(arr)
print(arr)
'''

#second method
'''
a=['school','car','hello','bet','apple','cat','bat']
for i in range(len(a)-1):
    for j in range(len(a)-1):
        if(a[j][0]>a[j+1][0]):
            a[j],a[j+1]=a[j+1],a[j]
        elif(a[j][0]==a[j+1][0] and a[j][1]>a[j+1][1]):
            a[j],a[j+1]=a[j+1],a[j]
print(a)
'''



'''
input:[[4,13,12],[8,10,5],[7,9,20],[14,8,3]]
ouput:[[14,8,3],[8,10,5],[7,9,20],[4,13,12]]
evary subarray as one prime number,sort them in according to prime numbers but it can be any index use bubble sort'''
'''
a = [[4,13,12],[8,10,5],[7,9,20],[14,8,3]]
for j in range(len(a)-1):
    f = False
    for i in range(len(a)-1-j):
        if a[i][0]<a[i+1][0]:
            a[i],a[i+1]=a[i+1],a[i]
            f = True
    if (f==False):
        break
print(a)
'''

#second method
#i/p : [[4,13,12],[8,10,5],[7,9,20],[14,8,3]], sort the matrix wrt prime no
#o/p:  [[14,8,3],[8,10,5],[7,9,20],[4,13,12]].
primes = []
matrix = [[4,13,12],[8,10,5],[7,9,20],[14,8,3]]
def isprime(n):
    if n < 2:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

def matrix_prime_sort(primes):
    n = len(matrix)
    for _ in range(n - 1):
        for i in range(n - 1):
            if primes[i] > primes[i + 1]:
                primes[i], primes[i + 1] = primes[i + 1], primes[i]
                matrix[i], matrix[i + 1] = matrix[i + 1], matrix[i]
    return matrix


r = len(matrix)
c = len(matrix[0])
for i in range(r):
    for j in range(c):
        if isprime(matrix[i][j]):
            primes.append(matrix[i][j])
print(primes)

print("Sorted matrix:", matrix_prime_sort(primes))






