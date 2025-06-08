#day-15
#stacks
'''write the program to calculate postfix'''
'''

a="15,3,+,6,2,-,*"

a=a.split(',')
s=[]
for i in a:
    if (i.isdigit()):
        s.append(int(i))
    else:
        u=s.pop()
        v=s.pop()
        if(i=='+'):
            s.append(v+u)
        elif(i=='-'):
            s.append(v-u)
        elif(i=='*'):
            s.append(v*u)
        elif(i=='/'):
            s.append(v/u)
        else:
            s.append(v**u)
print(s)
print(s[-1])
 '''
 
 
 
'''parenthesis check'''

'''
a="[({})]()"
s=[]
for i in range(len(a)):
    if(a[i] in {'(','{','['}):
        s.append(a[i])
    elif s:
        if(a[i]=='}' and s[-1]=='{'):
            s.pop()
        elif(a[i]==')' and s[-1]=='('):
            s.pop()
        elif(a[i]==']' and s[-1]=='['):
            s.pop()
        else:
            print("invalid")
    else:
        print("invalid")
        break
else:
    if(s):
        print("invalid")
    else:
        print("valid")
      
'''

      
    
            
        