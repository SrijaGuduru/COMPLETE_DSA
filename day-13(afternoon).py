#day-13
'''
print del kth node from the last'''
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
        
    def del_kth_node_from_last(self):
        slow = self.head
        fast = self.head
        k=3
        while k>0:
            fast=fast.next
            k-=1
        prev = None
        while fast!=None:
            prev=slow
            slow = slow.next
            fast = fast.next
        prev.next = slow.next
        

        
l1=linked()
l1.head=node(10)
l1.add_back(20)
l1.add_back(30)
l1.add_back(40)
l1.add_back(50)
l1.display()
l1.del_kth_node_from_last()
l1.display()       
'''


'''
make two nodes one pair and swap them
ip:10->20->30->40->50->60->70->none
op:20->10->40->30->60->50->70->none
'''
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
        
    def swap_pair(self):
        t=self.head
        while(t!=None and t.next!=None):
            t.data,t.next.data=t.next.data,t.data
            t=t.next.next
        
l1=linked()
l1.head=node(10)
l1.add_back(20)
l1.add_back(30)
l1.add_back(40)
l1.add_back(50)
l1.display()
l1.swap_pair()
l1.display()       
'''


'''perform the bubble sort in linkedlist
ip:9->3->10->11->2->5->6->4->1-<None
'''

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
        
    def bubble_sort(self):
        if self.head is None:
            return

        swapped = True
        while swapped:
            swapped = False
            t = self.head
            while t.next is not None:
                if t.data > t.next.data:
                    t.data, t.next.data = t.next.data, t.data
                    swapped = True
                t = t.next
l1=linked()
l1.head=node(50)
l1.add_back(20)
l1.add_back(10)
l1.add_back(30)
l1.add_back(40)
l1.display()
l1.bubble_sort()
l1.display()       
'''


'''check loop '''
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
        
    def check_loop(self):
        f=self.head
        s=self.head
        while(f!=None and f.next!=None):
            f=f.next.next
            s=s.next
            if(f==0):
                print("Loop")
                return
        print("No Loop")
l1=linked()
l1.head=node(50)
l1.add_back(20)
l1.add_back(10)
l1.add_back(30)
l1.add_back(40)
l1.display()
l1.check_loop()
l1.display()       
'''














