
#take number from the user check whether it is prime or not.
#not a prime number print not a prime number
#if it is prime number print whether it is greater 200 or lesser than 200
# Take input from the user

'''num = int(input("Enter a number: "))

is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    if num > 200:
        print("Prime number greater than 200")
    else:
        print("Prime number less than or equal to 200")
else:
    print("Not a prime number")'''
    


'''numbers = [8,2,3,4,3,3,4,5,6,7,9,2,4]
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
print("List after removing duplicates:", unique_numbers)'''


'''n = int(input())
output = ""
for i in range(1, n + 1):
    if i < n:
        output += str(i) + "+"
    else:
        output += str(i)
print(output)'''

#list=[2,3,4,3,2,5,5]

'''lst = [2, 3, 4, 3, 2, 5, 5]

for num in lst:
    if lst.count(num) == 1:
        print("The number that appears only once is:", num)
        break'''
        

#print(178<<13)
'''def even_or_odd(n):
    half = n // 2         # half = 4 // 2 = 2
    if half * 2 == n:     # 2 * 2 == 4 → True
        return "Even"
    else:
        return "Odd"
'''

#print(2^1)

'''def even_or_odd(n):
    if (n ^ 1) == n + 1:
        return "Even"
    else:
        return "Odd"
n=int(input())
print(even_or_odd(n))'''

'''n=int(input())
s=0
for i in range(1,n+1):
    s=s^i
print(s)'''



'''n=int(input())
if(n%4==1):
    print(1)
elif(n%4==2):
    print(n+1)
elif(n%4==3):
    print(0)
else:
    print(n)'''
    

'''def xorwhole(x):
    if(x%4==1):
        return 1
    elif(x%4==2):
        return x+1
    elif(x%4==3):
        return 0
    else:
        return x
n=int(input())
m=int(input())
print(xorwhole(n-1) ^ xorwhole(m))'''


#check whether the given number is power of 2 or not..sloution with less time complexity
'''def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

n=int(input())
print(is_power_of_two(n))'''


'''n=int(input())
if(n&n-1==0):
    print("yes")
else:
    print("no")'''


#find the number which occurs once in array   
'''arr=[2,2,4,4,6,6,7,8,8,9,9]
for i in range(0,len(arr),2):
    if(arr[i]!=arr[i+1]):
        print(arr[i])
        break'''
        


#length longest consecutive sequence
'''a=[1,2,3,2,3,4,5,6,7,8,9]
c=1
max=1
for i in range(len(a)-1):
    if(a[i]+1==a[i+1]):
        c=c+1
    else:
        if(c>max):
            max=c
        
        c=1
if(c<max):
    max=c
print(max)'''



#input:aaabbaaaacccddeff  
#output:a3b2a4c3d2e1f2

'''s=input()
count=1
result=""
for i in range(0,len(s)):
    if(s[i]==s[i-1]):
        count+=1
    else:
        result+=s[i-1]+str(count)
        count=1
result+=s[-1]+str(count)
print(result)'''


#recursion
'''def qwer(x):
    if(x==1):
        return  1
    return x*qwer(x-1)
b=qwer(5)
print(b)'''
            



'''def qwer(x):
    if(x==1):
        return 3
    if(x==2):
        return 1
    return qwer(x-1)+qwer(x-2)+x
b=qwer(5)
print(b)'''
        




'''def qwer(x):
    if(x==1):
        return 3
    if(x==2):
        return 1
    return qwer(x-1)+qwer(x-2)
b=qwer(8)
print(b)'''







    
    
    
    
    
   


    















    
