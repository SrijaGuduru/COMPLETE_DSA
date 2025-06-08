#day-20
'''
coin=[2,3,4,5]
amt=13
dp=[]
for i in range(len(coin)):
    dp.append([0]*(amt+1))
dp[0][0]=1
for i in range(len(coin)):
    dp[i][0]=1
dp[0][coin[0]]=1
for i in range(1,len(coin)):
    for j in range(1,amt+1):
        if(j<coin[i]):
            dp[i][j]!=dp[i-1][j]
        else:
            if(dp[i-1][j]==1):
                dp[i][j]=dp[i-1][j]
            else:
                if(dp[i-1][j-coin[i]==1]):
                    dp[i][j]=dp[i-1][j-coin[i]]
print(dp[i])
              
'''



'''
coin=[2,3,4,5]
ammount=13
dp=[[0]*(ammount+1) for i in range(len(coin))]
for i in range(len(coin)):
    dp[i][0]=1
for i in range(coin[0],ammount+1):
    dp[0][i]=dp[0][i-coin[0]]     
for i in range(1,len(coin)):
        for j in range(1,ammount+1):     
            if(j<coin[i]):
                dp[i][j]=dp[i-1][j]
            elif(dp[i-1][j]==1):
                 dp[i][j]=dp[i-1][j]
            elif(dp[i][j-coin[i]]==1):
                dp[i][j]=dp[i][j-coin[i]]
for i in dp:
    print(i)
if(dp[-1][-1]==1):
     print("Possible")
else:
     print("Not Possible")
 
 '''
 
'''1d matrix'''
'''
coin=[2,3,4,5]
amt=13
dp=[0]*(amt+1)
for i in range(len(coin)):
    for j in range(coin[i],amt+1):
        if (j==coin[i]):
            dp[j]=1
        if(dp[j]!=0 and dp[j-coin[i]!=0]):
            dp[j]=min(dp[j],1+dp[j-coin[i]])
        elif (dp[j-coin[i]]!=0):
            dp[j]=dp[j-coin[i]]+1
print(dp)
'''

'''length of longest common sub sequence in two strings,2d matrix
ip:ababd
   adabd
 op:4
   '''




#tries
class node:
    def __init__(self):
        self.data={}
        self.flag=False
        self.c=0
        
        

 
 
        