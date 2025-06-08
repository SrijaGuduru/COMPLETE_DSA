#day-11
#find the length of longest subarray with sum<=k
# i/p:[2,1,4,6,2,3,1,1,4,2,6,7,3], k=6
'''
a=[2,1,4,6,2,3,1,1,4,2,6,7,3]
k=6
l=0
m=0
sum=0
for r in range(len(a)):
    sum=sum+a[r]
    if(sum<=k):
        m=max(m,r-l+1)
    else:
        sum=sum-a[l]
        l=l+1
print(m)
'''


'''ip:ababba
lenth of longest palindrome substring,2 pointer approach
'''
'''
s="ababba"
m=0
for i in range(len(s)):
    l=i
    r=i
    while l>=0 and r<len(s)and s[l]==s[r]:
        m=max(m,r-l+1)
        l-=1
        r+=1
    l=i
    r=i+1
    while l>=0 and r<len(s)and s[l]==s[r]:
        m=max(m,r-l+1)
        l-=1
        r+=1
print(m)
'''



#print count of all the palindromic substring for a="abababa"
#output:10
'''
s="ababba"
m=0
c=0
for i in range(len(s)):
    l=i
    r=i
    while l>=0 and r<len(s)and s[l]==s[r]:
        m=max(m,r-l+1)
        l-=1
        r+=1
        c+=1
    l=i
    r=i+1
    while l>=0 and r<len(s)and s[l]==s[r]:
        m=max(m,r-l+1)
        l-=1
        r+=1
        c+=1
print(c)
'''

'''
ip:"abcdaecdb"
length of longest substring without repeating characters
'''





