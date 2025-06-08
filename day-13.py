#day-13
#linkedlist
'''
class node:
    def __init__(self):
        self.data=10
        self.next=None
a=node()
print(a.data,a.next)
'''

#linkedlist
'''
class node:
    def __init__(self,u):
        self.data=u
        self.next=None
class linked:
    def __init__(self):
        self.head=None
    def add_back(self,x):
        t=self.head
        while(t.next!=None):
            t=t.next
        t.next=node(x)
    def display(self):
        t=self.head
        while (t!=None):
            print(t.data,end='->')
            t=t.next
        print('None')
l1=linked()
l1.head=node(10)
l1.add_back(20)
l1.add_back(30)
l1.add_back(40)
l1.add_back(50)
l1.display()
        
'''        
        
'''
sum 0f node in linkedlist
'''
'''
class node:
    def __init__(self,d):
        self.data = d
        self.next = None
class linked:
    def __init__(self):
        self.head = None
    def add_back(self,x):
        t = self.head
        while t.next != None:
            t = t.next
        t.next = node(x)
    def display(self):
        t=self.head
        while t!=None:
            print(t.data,"->",end=" ")
            t=t.next
        print(None)
    def sum_nodes(self):
        t=self.head
        tot_sum = 0
        while t!=None:
            tot_sum += t.data
            t=t.next
        print(tot_sum)
    


l1 = linked()
l1.head = node(5)
l1.add_back(20)
l1.add_back(30)
l1.add_back(45)
l1.add_back(100)
l1.display()
l1.sum_nodes()
'''



'''
sum of all even numbers'''
'''
class node:
    def __init__(self,u):
        self.data=u
        self.next=None
class linked:
    def __init__(self):
        self.head=None
    def add_back(self,x):
        t=self.head
        while(t.next!=None):
            t=t.next
        t.next=node(x)
    def display(self):
        t=self.head
        while (t!=None):
            print(t.data,end='->')
            t=t.next
        print('None')
    def sum_all_even(self):
        t=self.head
        s=0
        while(t!=None):
            if(t.data%2==0):
                s=s+t.data
            t=t.next
        print(s)
l1=linked()
l1.head=node(10)
l1.add_back(20)
l1.add_back(30)
l1.add_back(40)
l1.add_back(50)
l1.display()
l1.sum_all_even()
'''


'''sum of data even position'''
#wrong
'''
class node:
    def __init__(self,u):
        self.data=u
        self.next=None
class linked:
    def __init__(self):
        self.head=None
    def add_back(self,x):
        t=self.head
        while(t.next!=None):
            t=t.next
        t.next=node(x)
    def display(self):
        t=self.head
        while (t!=None):
            print(t.data,end='->')
            t=t.next
        print('None')
    def sum_all_even_position(self):
        t=self.head
        s=0
        pos=1
        while(t!=None):
            if(pos%2==0):
                s=s+t.data
                pos=pos+1
            t=t.next
        print(s)
l1=linked()
l1.head=node(10)
l1.add_back(20)
l1.add_back(30)
l1.add_back(40)
l1.add_back(50)
l1.display()
l1.sum_all_even_position()
'''


'''
find second largest number in the linked list'''
'''
class node:
    def __init__(self,d):
        self.data = d
        self.next = None
class linked:
    def __init__(self):
        self.head = None
    def add_back(self,x):
        t = self.head
        while t.next != None:
            t = t.next
        t.next = node(x)
    def display(self):
        t=self.head
        while t!=None:
            print(t.data,"->",end=" ")
            t=t.next
        print(None)
    def second_largest(self):
        first=second=float('-inf')
        t=self.head
        while t:
            if t.data>first:
               second=first
               first=t.data
            elif t.data!=first and t.data>second:
                second=t.data
            t=t.next
            
        print(second)

l1 = linked()
l1.head = node(5)
l1.add_back(20)
l1.add_back(30)
l1.add_back(45)
l1.add_back(100)
l1.display()
l1.second_largest()
'''


'''count of consecutive pairs of sum k'''
#wrong
'''
class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_back(self, x):
        if self.head is None:
            self.head = Node(x)
            return
        t = self.head
        while t.next:
            t = t.next
        t.next = Node(x)

    def display(self):
        t = self.head
        while t:
            print(t.data, "->", end=" ")
            t = t.next
        print("None")

    def count_consecutive_sum(self, k):
        count = 0
        t = self.head
        while t and t.next:
            if t.data + t.next.data == k:
                count += 1
            t = t.next
        print(count)

l1 = LinkedList()
l1.add_back(1)
l1.add_back(4)
l1.add_back(5)
l1.add_back(2)
l1.add_back(3)
l1.add_back(6)
l1.add_back(5)
l1.add_back(8)
l1.display()
l1.count_consecutive_sum(10)
'''




'''count of all possible pairs whose count is lesser than equal to k'''
'''
class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_back(self, x):
        if self.head is None:
            self.head = Node(x)
            return
        t = self.head
        while t.next:
            t = t.next
        t.next = Node(x)

    def display(self):
        t = self.head
        while t:
            print(t.data, "->", end=" ")
            t = t.next
        print("None")

    def count_all_pairs_sum(self, k):
        count = 0
        t = self.head
        while t:
            t1 = t.next
            while t1:
                if t.data + t1.data <= k:
                    count += 1
                t1 = t1.next
            t = t.next
        print(count)


l1 = LinkedList()
l1.add_back(1)
l1.add_back(4)
l1.add_back(5)
l1.add_back(2)
l1.add_back(3)
l1.add_back(6)
l1.add_back(5)
l1.add_back(8)

l1.display()
l1.count_all_pairs_sum(10)
'''



'''print second half of the linkedlist'''
'''
class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_back(self, x):
        if self.head is None:
            self.head = Node(x)
            return
        t = self.head
        while t.next:
            t = t.next
        t.next = Node(x)

    def display(self):
        t = self.head
        while t:
            print(t.data, "->", end=" ")
            t = t.next
        print("None")
    def print_second_half(self):
        t1 = t = self.head
        while t and t1.next:
            t1 = t1.next
            t = t.next.next

        
        
        while t1:
            print(t1.data, "->", end=" ")
            t1 = t1.next
        print("None")
    


l1 = LinkedList()
l1.add_back(1)
l1.add_back(4)
l1.add_back(5)
l1.add_back(2)
l1.add_back(3)
l1.add_back(6)
l1.add_back(5)
l1.add_back(8)

l1.display()
l1.print_second_half()
'''


'''
print the first half of the LinkedList
'''
'''
class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_back(self, x):
        if self.head is None:
            self.head = Node(x)
            return
        t = self.head
        while t.next:
            t = t.next
        t.next = Node(x)

    def display(self):
        t = self.head
        while t:
            print(t.data, "->", end=" ")
            t = t.next
        print("None")

    def print_first_half(self):
        
        slow = fast = self.head
        count = 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            count += 1

        
        t = self.head
        print("First half of the list:")
        for _ in range(count):
            print(t.data, "->", end=" ")
            t = t.next
        print("None")

l1 = LinkedList()
l1.add_back(1)
l1.add_back(4)
l1.add_back(5)
l1.add_back(2)
l1.add_back(3)
l1.add_back(6)
l1.add_back(5)
l1.add_back(8)

l1.display()
l1.print_first_half()
'''


'''
print kth node from the last'''
class node:
    def __init__(self,u):
        self.data=u
        self.next=None
class linked:
    def __init__(self):
        self.head=None
    def add_back(self,x):
        t=self.head
        while(t.next!=None):
            t=t.next
        t.next=node(x)
    def display(self):
        t=self.head
        while (t!=None):
            print(t.data,end='->')
            t=t.next
        print('None')
        
    def print_kth_from_end(self, k):
        first = second = self.head
        for _ in range(k):
            if first is None:
            
                return
            first = first.next

        while first:
            first = first.next
            second = second.next

        print(second.data)

        
l1=linked()
l1.head=node(10)
l1.add_back(20)
l1.add_back(30)
l1.add_back(40)
l1.add_back(50)
l1.display()
l1.print_kth_from_end(3)
        

