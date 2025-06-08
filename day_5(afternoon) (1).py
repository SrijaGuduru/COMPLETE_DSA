#day-5
'''
#land and fire problem
input:1 0 0 1 1 1
      1 1 1 0 0 0
      0 0 1 1 1 1
      1 1 1 0 0 0
      0 0 0 0 0 1
      1 0 0 1 0 0
output:6
'''
'''
def tree(a,i,j,n):
    if i==n or j==n or i<0 or j<0 or a[i][j]==0 or a[i][j]==2:
        return 0
    if a[i][j]==1:
        a[i][j]=2
    tree(a,i-1,j,n) #top
    tree(a,i,j-1,n) #left
    tree(a,i+1,j,n) #down
    tree(a,i,j+1,n) #right

c=0
a=[[1,0,0,1,1,1],[1,1,1,0,0,0],[0,0,1,1,1,1],[1,1,1,0,0,0],[0,0,0,0,0,1],[1,0,0,1,0,0]]
tree(a,2,5,6)
for i in range(6):
    for j in range(6):
        if a[i][j]==1: 
            c+=1
print(c)
 '''
 

#frog jump problem
'''
intput:5
       2,3
       [(2,1),(4,1),(5,3),(3,5)]->should not jump
       can move only right to bottom
       how many ways to reach corner bottom'''
'''
def frog(n,i,j,hud):
    if(i==n or j==n or (i,j) in hud):
        return 0
    if(i==n-1 and j==n-1):
        return 1
    return frog(n,i+j,j,hud) + frog(n,i,j+1,hud)
n=5
i=2
j=3
hud=[(2,1),(4,1),(5,2),(3,5)]
print(frog(n,i-1,j-1,hud))
'''



#if a integer is given print binary values untill that integer
'''input:3
output:00
       01
       10
       11'''
'''import math
def allbinary(a,n,s=''):
    if(len(s)==n):
        print(s)
        return
    allbinary(a,n,s+'0')
    allbinary(a,n,s+'1')


a=7
n=int(math.log(a,2))+1
allbinary(a,n)'''




#second classmethod
'''
import math
def allbinary(a,n,s=''):
    if a==1:
        return a
    if(len(s)==n):
        print(s)
        a=a-1
        return a
    a=allbinary(a,n,s+'0')
    a=allbinary(a,n,s+'1')
    return a

a=18
n=int(math.log(a,2))+1
allbinary(a,n)'''



#if three inputs print the possiblr parenthasis
def generate_parentheses(n, open_count=0, close_count=0, current=""):
    if len(current) == 2 * n:
        print(current)
        return
    
    if open_count < n:
        generate_parentheses(n, open_count + 1, close_count, current + "(")
    if close_count < open_count:
        generate_parentheses(n, open_count, close_count + 1, current + ")")


if __name__ == "__main__":
    n = int(input("Enter number of pairs of parentheses: "))
    generate_parentheses(n)
















