#day_6
#second method
#i/p : [[4,13,12],[8,10,5],[7,9,20],[14,8,3]], sort the matrix wrt prime no
#o/p:  [[14,8,3],[8,10,5],[7,9,20],[4,13,12]].
'''
def prime(x):
    for i in x:
        for j in range(2,int(i**0.5)+1):
            if(i%j==0):
                break
        else:
            return i
a=[[4,13,12],[8,10,5],[7,9,20],[14,8,3]]
b=[]
for i in a:
    b.append(prime(i))
for i in range(len(b)-1):
    f=0
    for j in range(len(b)-1-i):
        if(b[j]>b[j+1]):
            b[j],b[j+1]=b[j+1],b[j]
            a[j],a[j+1]=a[j+1],a[j]
            f=1
    if(f==0):
        break
print(a)
'''



'''input:an apple a day keeps doctor away
output:a an day away apple keeps doctor

take sentence from the user ,sort according to word length and print them as a sentence.use bubble sort'''
'''
sentence = input()
words = sentence.split()
n=len(words)
word_lengths = [len(word) for word in words]

for i in range(n):
    for j in range(0,n-i-1):
        if word_lengths[j]>word_lengths[j+1]:
            word_lengths[j],word_lengths[j+1]=word_lengths[j+1],word_lengths[j]
            words[j],words[j+1]=words[j+1],words[j]
            
output=' '.join(words)
print(output)
'''

#second method
'''
a="an apple a day keeps doctor away".split()
b=[]
for i in a:
    b.append(len(i))
for i in range(len(b)-1):
    f=0
    for j in range(len(b)-1-i):
        if(b[j]>b[j+1]):
            b[j],b[j+1]=b[j+1],b[j]
            a[j],a[j+1]=a[j+1],a[j]
            f=1
    if(f==0):
        break
print(' '.join(a))
'''



'''input:[7,2,6,3,6,7,7,2,2,2]
output:[3,6,6,7,7,7,2,2,2,2]
sort them depending on frequencies but dont use count function
'''
'''
arr = [7, 2, 6, 3, 6, 7, 7, 2, 2, 2]
frequency={}
for num in arr:
    if num in frequency:
        frequency[num]+=1
    else:
        frequency[num]=1
n=len(arr)
for i in range(n):
    for j in range(0,n-i-1):
        if frequency[arr[j]] > frequency[arr[j + 1]]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print(arr)
 '''
 
'''
a=[4,4,4,7,3,2,2,3,1,5,6,8,9,2,1,1]
o/p:[7,6,8,9,4,4,5,5,3,3,2,2,2,1,1,1]
'''
'''    
a=[3,5,4,4,5,6,7,7,8,8,7,6,4,1,1,2,8,8]
d={}
for i in a:
    if(i not in d):
        d[i]=1
    else:
        d[i]+=1
print(d)
n=max(d.values())
b=[]
for i in range(n+1):
    b.append([])
print(b)
for i in d.items():
    b[i[1]].append(i[0])
print(b)
c=[]
for i in range(len(b)):
    for j in b[i]:
        c.extend([j]*i)
print(c)
'''
