#day-14
'''
reverse the half of the linkedlist
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
    def reverse_half(self):
        f=self.head
        s=self.head
        while(f!=None and f.next!=None):
            f=f.next.next
            pr=s
            s=s.next
        p=None
        c=s
        while(c!=None):
            n = c.next
            c.next = p
            p = c
            c = n
        pr.next=p

l1=linked()
l1.head=node(10)
l1.add_back(20)
l1.add_back(30)
l1.add_back(40)
l1.add_back(50)
l1.add_back(60)
l1.display()
l1.reverse_half()
l1.display()
'''






'''find the intersecting two linkedlist'''
'''
class node:
    def __init__(self, u):
        self.data = u
        self.next = None

class linked:
    def __init__(self):
        self.head = None

    def add_back(self, x):
        t = self.head
        while t.next:
            t = t.next
        t.next = node(x)

    def display(self):
        t = self.head
        while t:
            print(t.data, end='->')
            t = t.next
        print('None')

def get_length(head):
    count = 0
    while head:
        count += 1
        head = head.next
    return count

def get_intersection(head1, head2):
    len1, len2 = get_length(head1), get_length(head2)

    
    if len1 > len2:
        for _ in range(len1 - len2):
            head1 = head1.next
    else:
        for _ in range(len2 - len1):
            head2 = head2.next

    
    while head1 and head2:
        if head1 == head2:  
            return head1.data
        head1 = head1.next
        head2 = head2.next
    return None
l1 = linked()
l1.head = node(10)
l1.add_back(20)
l1.add_back(30)
l1.add_back(40)
l1.add_back(50)
l1.add_back(60)

l2 = linked()
l2.head = node(100)
l2.head.next = node(200)
l2.head.next.next = node(300)
l2.head.next.next.next = l1.head.next.next.next  
intersect = get_intersection(l1.head, l2.head)
print(intersect if intersect else "No intersection")
'''


