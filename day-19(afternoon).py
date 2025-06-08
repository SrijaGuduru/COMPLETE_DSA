#day-19
'''
[(1,3),(2,5),(4,6),(6,7),(5,8),(7,9)] ->these are timings
[5,6,5,4,11,2]->time slots
using dynamic programming,given timings and time slots,this are the money we earn by doing above jobs what was the maximum money

'''
'''
a=[(1,3),(2,5),(4,6),(6,7),(5,8),(7,9)]
pr=[5,   6,   5,   4,  11,  2]
dp=pr.copy()
for j in range(1,len(pr)):
    for i in range(j):
        if(a[i][1]<=a[j][0]):
            dp[j]=max(dp[j],pr[j]+dp[i])
print(dp)
'''




