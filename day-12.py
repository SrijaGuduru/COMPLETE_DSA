#day-12
#leet code questions
'''
ip:'abcdecfbgce'
take dictionary,if not in dictionay change your l and update your l.
constraits:m=max(m,r-l+1)
output:6
'''
'''
def longest_unique_substring(s):
    last_seen = {}
    l = 0
    max_len = 0

    for r in range(len(s)):
        if s[r] in last_seen and last_seen[s[r]] >= l:
            l = last_seen[s[r]] + 1
        last_seen[s[r]] = r
        max_len = max(max_len, r - l + 1)

    return max_len


s = 'abcdecfbgce'
print(longest_unique_substring(s))  
'''

'''
ip:'abcdecfbgce'
m='c'
n='d'
length of subarray of not repeating character ,but it should contain m and n values.
output:5
'''
'''
a="abcdefbg"
l=0
m=0
res=""
u,v='c','d'
d={}
for r in range(len(a)):
    if (a[r] not in d):
        l=d[a[r]]=r
    else:
        if(d[a[r]]>=1):
            l=d[a[r]]+1
        d[a[r]]=r
    if (r-l+1>m and u in d and v in d and d[u]>=l and d[v]>=l):
        m=r-l+1
        res=1
        res=a[l:r+1]
#     m=max(m,r-l+1)
print(res)
print(m)
'''

'''
ip:[4,2,7,20,8,6,4,1] (these are deck of cards)
k=3  (no.of cards should be removed)
output:16
use greedy algorithm
remove cards from top or bottom,and print max of cards
'''

#leet code question
'''
a=[4,3,2,5,6,1,12,3]
k=4
n=len(a)
sl=0
for i in range(k):
    sl=sl+a[i]
sr=0
m=sl
for i in range(k-1,-1,-1):
    sl=sl-a[i]
    sr=sr+a[n-1]
    m=max(m,sl+sr)
    n=n-1
#     print(sl,sr)
print(sr)
'''







