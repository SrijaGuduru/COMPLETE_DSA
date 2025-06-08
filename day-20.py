#day-20
#dynamic programming
'''coins
1.create a 2d dp table with zeros
2.fill row-0 directly
3.fill 0th clounm completely
4.start from row 1
'''
'''

coin=[2,3,4,5]
amt=13
dp=[[0]+(amt+1)]*len(coin)
dp=[[0]*(amt+1) for i in range(len(coin))]
'''
'''for i in range(len(coin)):
    dp.append([0]*(amt+1))
dp[0][0]=1'''
'''
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



#second classmethod
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



'''print the minimum number of coins'''


coin=[2,3,4,5]
amount=12
dp=[]
for i in range(len(coin)):
    dp.append([0]*(amount+1))
dp[0][coin[0]]=1
for i in range(1,len(coin)):
    for j in range(1,amount+1):
        if j<coin[i]:
            dp[i][j]=dp[i-1][j]
        elif(coin[i]==j):
            dp[i][j]=1
        else:
            if(dp[i-1][j]!=0 and dp[i-1][j-coin[i]]!=0):
                k=min(1+dp[i-1][j-coin[i]],dp[i-1][j])
                dp[i][j]=k
            elif(dp[i-1][j]!=0):
                dp[i][j]=dp[i-1][j]
            elif(dp[i-1][j-coin[i]]!=0):
                dp[i][j]=1+dp[i-1][j-coin[i]]
for i in dp:
    print(i)
    
    
    
    
