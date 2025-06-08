#day-19
#dynamic programming
#fibonacci series
'''
def fibo(n):
    if(dp[n-1]!=-1):
        return dp[n-1]
    if(n==1):
        return 1
    if(n==2):
        return 1
    dp[n-1]=fibo(n-1)+fibo(n-2)
    return dp[n-1]
dp=[1,1,-1,-1,-1,-1,-1]
fibo(7)
print(dp)
'''

'''
dp=[1,1]
for i in range(2,7):
    dp.append(dp[i-1]+dp[i-2])
print(dp[7-1])
'''


'''
f1=1
f2=1
ans=0
for i in range(2,7):
    ans=f1+f2
    f1=f2
    f2=ans
print(ans)
'''



'''frog jump
ip:[10,20,30,10]
op:20
'''

'''
def frog_jump(heights):
    n = len(heights)
    dp = [0] * n
    dp[0] = 0
    dp[1] = abs(heights[1] - heights[0])
    for i in range(2, n):
        one_step = dp[i-1] + abs(heights[i] - heights[i-1])
        two_steps = dp[i-2] + abs(heights[i] - heights[i-2])
        dp[i] = min(one_step, two_steps)
    
    return dp[-1]
heights = [10, 20, 30, 10]
print(frog_jump(heights))  
'''

'''using recursion'''
'''
def frog(n):
    if(n<=1):
        return dp[n]
    dp[n]=min(frog(n-1)+abs(a[n]-a[n-1]),(frog(n-2)+abs(a[n]-a[n-2])))
    return dp[n]
a=[10,20,30,10,30,20,10]
dp = [-1] * len(a)
dp[0] = 0
dp[1] = abs(a[1] - a[0])

frog(6)
print(dp)
'''


'''same question with tabulation'''
'''
a=[10,20,30,10,30,20,10]
dp=[0]*len(a)
dp[1]=abs(a[0]-a[1])
for i in range(2,len(a)):
    dp[i]=min((dp[i-1]+abs(a[i]-a[i-1]),(dp[i-2]+abs(a[i]-a[i-2]))))
print(dp[len(a)-1])
'''


'''remove tabulation and keep variable k=2 '''
'''
a=[10,20,30,10,30,20,10]
dp=[9999]*len(a)
dp[1]=abs(a[0]-a[1])
k=2
for i in range(2,len(a)):
    for j in range(1,k+1):
        temp=dp[i-j]+abs(a[i]-a[i-j])
        dp[i]=min(temp,dp[i])
print(dp[len(a)-1])
'''


