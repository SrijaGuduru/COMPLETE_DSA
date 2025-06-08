#day-8
#search an element in the matrix
'''
def search_matrix(matrix,target):
    found=False
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==target:
                found=True
                break
        if found:
            break
    if not found:
        print(f"Element {target} not found in the matrix.")


matrix = [
    [3, 8, 4],
    [1, 9, 2],
    [7, 6, 5]
]

search_matrix(matrix, 9)
'''


#second classmethod
'''
a=[[2,8,7],[9,5,7],[1,3,4]]
x=5
n=3
for i in range(n):
    f=0
    for j in range(n):
        if(a[i][j]==x):
            print("found")
            f=1
            break
    if(f==1):
        break
    
else:
    print("not found")
'''




#another question
'''[2  3   7   8
    9 15  20   22 
   23 26  35   37
   38 39  42   43]
'''
'''
def matrix_bs(matrix,t):
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        if matrix[i][0]< t and matrix[i][cols-1]>=t:
            return binary_serach(matrix[i],rows,t)
def binary_serach(row,rows,t):
    l=0
    r=len(row)-1
    while l<=r:
        m=(l+r)//2
        if row[m]<t:
            l=m+1
        elif row[m]>t:
            r=m-1
        else:
            return m,rows
    return -1
matrix=[[2,3,7,8],[9,15,20,22],[23,26,35,37],[38,39,42,43]]
t=35
print(matrix_bs(matrix,t))
'''



#second classmethod
'''
a=[[2,3,7,8],[9,15,20,22],[23,26,35,37],[38,39,42,43]]
n=3
m=4
x=17
l=0
r=(n+m)-1
while(l<=r):
    mid=(l+r)//2
    if(a[mid//m][mid%m]==x):
        print("found")
        break
    elif(x<a[mid//m][mid%m]):
        r=mid-1
    else:
        l=mid+1
else:
    print("not found")
'''


#another question
'''shippacakages question
ip:[1,2,3,4,5,6,7,8,9,10]
capacity=12
op:6
print whether it is possible or not'''
            

def can_ship(weights,capacity,target_day):
    current_load=0
    days=1
    for weight in weights:
        if weight>capacity:
            return False
        if current_load+weight>capacity:
            days+=1
            current_load=0
        current_load+=weight
    return days<=target_day
weights = [1,2,3,4,5,6,7,8,9,10]
capacity = 12
target_day= 6
if can_ship(weights,capacity,target_day):
    print("possible to ship within",target_day,"days")
else:
    print(" not possible to ship within",target_day,"days")
            







                