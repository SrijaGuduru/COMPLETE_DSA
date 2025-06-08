#DAY-11
'''ip:[0,3,8,1,5,7,9] starting of meeting
      [5,6,10,2,6,9,11] ending of meeting
given array is timings of meeting,print max no of meetings conducted and each meeting should have atleast one hour gap between.
use jobs scheduling algorithm,sort respect to end time.
'''
'''
start=[0,3,8,1,5,7,9]
end=[5,6,10,2,6,9,11]
meetings=[]
for i in range(len(start)):
    meetings.append(start[i],end[i])
for i in range(len(meetings)):
    for j in range  for j in range(i + 1, len(meetings)):
        if meetings[i][1] > meetings[j][1]:
            meetings[i], meetings[j] = meetings[j], meetings[i]

count=0
last_end=-1
for s,e in meetings:
    if s>=last_end+1:
        count+=1
        last_end=e
print(count)
'''

#second classmethod
'''
def func(x):
    return x[1]
s=[0,3,8,1,5,7,9]
e=[5,7,10,2,6,9,11]
b=list(zip(s,e))
b.sort(key=func)
st=0
c=0
for i in b:
    if(i[0]>=st):
        c=c+1
        st=i[1]+1
print(c)    
'''



'''
ip:"hippopotamus"
[s,i,m,t,o,p,p,o,a,p,u,h]
op:simtoppoapuh
reverse the string withour changing the vowels position'''
'''
def reverse_except_vowels(s):
    vowels = 'aeiouAEIOU'
    s_list = list(s)
    vowel_positions = [i for i, ch in enumerate(s_list) if ch in vowels]
    consonants = [ch for ch in s_list if ch not in vowels]
    consonants.reverse()
    result = []
    consonant_index = 0
    for i in range(len(s_list)):
        if i in vowel_positions:
            result.append(s_list[i])  
        else:
            result.append(consonants[consonant_index])
            consonant_index += 1
    return ''.join(result)
input_str = "hippopotamus"
output = reverse_except_vowels(input_str)
print(output)
'''



'''
ip:[2,1,6,4,2,3,1,1,4,2,6,7,3]  these are discounts of books
there are few books with discounts given in array ,pick the five contiguous books without breaking chain ,
print the max discounts'''
'''
def max_discounts(discounts):
    max_sum=current_sum=sum(discounts[:5])
    for i in range(5,len(discounts)):
        current_sum=current_sum-discounts[i-5]+discounts[i]
        max_sum=max(max_sum,current_sum)
    return max_sum
discounts=[2,1,6,4,2,3,1,1,4,2,6,7,3]
print(max_discounts(discounts))
''' 

'''
ip:[2,1,6,4,2,3,1,1,4,2,6,7,3]
print the len longest subarray (sum<=k)
k=6
m=max(m,r-l+1)
'''
#find the length of longest subarray with sum<=k
# i/p:[2,1,4,6,2,3,1,1,4,2,6,7,3], k=6
'''
def longest_subarray_ksum(arr):
    curr_sum = 0
    k=7
    i=0
    length,max_len=0,0
    for j in range(len(arr)):
        curr_sum += arr[j]
        if curr_sum <= k:
            length = j-i+1
            max_len = max(length,max_len)
        while curr_sum>k:
            curr_sum -= arr[i]
            i+=1
    return max_len

arr=[2,1,4,6,2,3,1,1,4,2,6,7,3]
print(longest_subarray_ksum(arr))
 '''
 








