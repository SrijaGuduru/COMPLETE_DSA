#day_5
'''input:[2,4,1,5,8,4,7] it contains uniquevalues and duplicate values
output:7
example :given array cost of each day in week.a person buying pen for min rate and selling it to max rate .
condition is he should buy and sell only once.and find profit.
find the min element from array and max element from array and find difference of both.
use only two for loops and use greedy algorithm.
'''

        
'''prices = [2, 4, 1, 5, 8, 4, 7]
max_profit = 0

for i in range(len(prices)):
    buy_price = prices[i]
    for j in range(i + 1, len(prices)):
        sell_price = prices[j]
        profit = sell_price - buy_price
        if profit > max_profit:
            max_profit = profit

print(max_profit)  
'''



#second classmethod
'''a=[4,5,6,2,3,14,5,6,4]
m=0
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if(a[j]-a[i]>m):
            m=a[j]-a[i]
print(m)'''



#another classmethod
#own solution
'''a=[13,14,2,5,18,1,4]
b=0
m=0
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if(a[i]<a[j]):
          b=a[i]
          if(a[j]-a[i]>m):
             m=a[j]-a[i]
print(m)'''




'''[1 0 0 1 1
    1 0 0 0 1
    0 0 0 0 1
    0 0 0 1 0
    1 0 0 0 0
    1 0 0 0 1]
  given matrix where all 1's are lands and 0's are water,if more than 1 is together then consider those as grouplands
  print no of such group lands'''
'''grid = [
    [1, 0, 0, 1, 1],
    [1, 0, 0, 0, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 1]
]

rows = len(grid)
cols = len(grid[0])
visited = [[False for _ in range(cols)] for _ in range(rows)]

# Directions: up, down, left, right
directions = [(-1,0), (1,0), (0,-1), (0,1)]

def dfs(r, c):
    visited[r][c] = True
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            if not visited[nr][nc] and grid[nr][nc] == 1:
                dfs(nr, nc)

# Count connected components
count = 0
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == 1 and not visited[i][j]:
            dfs(i, j)
            count += 1

print(count)  # Output: 5
'''

#second classmethod
'''
def land(a,i,j,n):
    if (i==n or j==n or i<0 or j<0 or a[i][j]==0 or a[i][j]==2):
        return 0
    if (a[i][j]==1):
        a[i][j]=2
    land(a,i-1,j,n)
    land(a,i,j-1,n)
    land(a,i,j+1,n)
    land(a,i+1,j,n)
a=[[1, 0, 0, 1, 1],
   [1, 0, 0, 0, 1],
   [0, 0, 0, 1, 0],
   [1, 0, 0, 0, 0],
   [1, 0, 0, 0, 1]]
for i in a:
    print(i)
c=0
for i in range (5):
    for j in range(5):
        if (a[i][j]==1):
            land(a,i,j,5)
            c=c+1
print(c)

'''

'''array=[8,7,6,5,2]
[0 1 1 0 1
 1 1 0 0 1
 0 0 0 1 1
 0 1 0 0 0]
 in matrix in place of print the same index value from array and add each row ,print the output
after replacing with array elements matrix is:
[0 7 6 0 2
 8 7 0 0 2
 0 0 0 5 2
 0 7 0 0 0]
 output:15 
        17
        7
        7 '''

'''arr=[8, 7, 6, 5, 2]
matrix=[[0, 1, 1, 0, 1],
        [1, 1, 0, 0, 1],
        [0, 0, 0, 1, 1],
        [0, 1, 0, 0, 0]]
result=[]
for row in matrix:
    total=0
    for j in range(len(row)):
        if row[j]==1:
            total+=arr[j]
    result.append(total)
for n in result:
    print(n)'''
    



'''[0 1 1 0 1
    1 1 0 0 1
    0 0 0 1 1
    0 1 0 0 0]
if 1 is their stop over there itself.in same way count no .of paths.use recursion
'''
