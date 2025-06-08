#day-16
'''search node in bst'''
'''
class node:
    def __init__(self,u):
        self.data=u
        self.left=None
        self.right=None
    def inorder(self,root):
        if(root==None):
            return
        print(root.data,end=" ")
        self.inorder(root.left)
        
        self.inorder(root.right)
    def search_in_tree(self,root,t):
        if root == None:
            return
        if root.data == t:
            return root.data
        elif root.data > t:
            return self.search_in_tree(root.left,t)
        else:
            return self.search_in_tree(root.right,t)
root = node(10)
root.left = node(5)
root.right = node(20)
root.left.right = node(8)
root.left.left = node(2)
#root.inorder(root)
print(root.search_in_tree(root,22))
'''


'''
insertion'''
'''
class Node:
    def __init__(self, u):
        self.data = u
        self.left = None
        self.right = None

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

def search_in_tree(root, t):
    if root is None:
        return None
    if root.data == t:
        return root.data
    elif root.data > t:
        return search_in_tree(root.left, t)
    else:
        return search_in_tree(root.right, t)

def insert(root, x):
    if root is None:
        return Node(x)
    if x < root.data:
        root.left = insert(root.left, x)
    else:
        root.right = insert(root.right, x)
    return root


root = None
root = insert(root, 10)
root = insert(root, 5)
root = insert(root, 2)
root = insert(root, 20)
root = insert(root, 8)
inorder(root) 
'''

   




'''count the no of leaf node in bst'''
'''
class Node:
    def __init__(self, u):
        self.data = u
        self.left = None
        self.right = None

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

def search_in_tree(root, t):
    if root is None:
        return None
    if root.data == t:
        return root.data
    elif root.data > t:
        return search_in_tree(root.left, t)
    else:
        return search_in_tree(root.right, t)

def insert(root, x):
    if root is None:
        return Node(x)
    if x < root.data:
        root.left = insert(root.left, x)
    else:
        root.right = insert(root.right, x)
    return root


root = None
root = insert(root, 10)
root = insert(root, 5)
root = insert(root, 2)
root = insert(root, 20)
root = insert(root, 8)
inorder(root) 
'''

   




'''count the no of leaf node in bst'''
'''

class node:
    def __init__(self,u):
        self.data=u
        self.left=None
        self.right=None
def inorder(self,root):
    if(root==None):
        return
    print(root.data,end=" ")
    self.inorder(root.left)
        
    self.inorder(root.right)
def search_in_tree(self,root,t):
    if root == None:
        return
    if root.data == t:
        return root.data
    elif root.data > t:
        return self.search_in_tree(root.left,t)
    else:
        return self.search_in_tree(root.right,t)
def insert(root,x):
    if(root==None):
        return node(x)
    if(x<root.data):
        root.left=insert(root.left,x)
    else:
        root.right=insert(root.right,x)
    return root
def count_leaf_node(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return count_leaf_node(root.left) + count_leaf_node(root.right)

    
root=None
root=insert(root,10)
root=insert(root,5)
root=insert(root,2)
root=insert(root,20)
root=insert(root,8)
print(count_leaf_node(root))
'''

'''find the cout of all the paths'''
'''
class Node:
    def __init__(self, u):
        self.data = u
        self.left = None
        self.right = None

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

def search_in_tree(root, t):
    if root is None:
        return None
    if root.data == t:
        return root.data
    elif root.data > t:
        return search_in_tree(root.left, t)
    else:
        return search_in_tree(root.right, t)

def insert(root, x):
    if root is None:
        return Node(x)
    if x < root.data:
        root.left = insert(root.left, x)
    else:
        root.right = insert(root.right, x)
    return root
def all_paths(root,l):
    if(root==None):
        return 
    l.append(root.data)
    if(root.left==None and root.right==None):
        print(l)
        l.pop()
        return
    all_paths(root.left,l)
    all_paths(root.right,l)
    l.pop()
        
            

root = None
root = insert(root, 10)
root = insert(root, 5)
root = insert(root, 2)
root = insert(root, 20)
root = insert(root, 8)
print(all_paths(root,[]))
'''


'''level order traversal'''
'''
class Node:
    def __init__(self, u):
        self.data = u
        self.left = None
        self.right = None

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

def search_in_tree(root, t):
    if root is None:
        return None
    if root.data == t:
        return root.data
    elif root.data > t:
        return search_in_tree(root.left, t)
    else:
        return search_in_tree(root.right, t)

def insert(root, x):
    if root is None:
        return Node(x)
    if x < root.data:
        root.left = insert(root.left, x)
    else:
        root.right = insert(root.right, x)
    return root
def all_paths(root,l):
    if(root==None):
        return 
    l.append(root.data)
    if(root.left==None and root.right==None):
        print(l)
        l.pop()
        return
    all_paths(root.left,l)
    all_paths(root.right,l)
    l.pop()
def level(root,l):
    if root==None:
        return
    l.append(root)
    while(l):
        curr=l.pop(0)
        if(curr.left!=None):
            l.append(curr.left)
        if(curr.right!=None):
            l.append(curr.right)
        print(curr.data,end=" ")
        
            
root = None
root = insert(root, 10)
root = insert(root, 5)
root = insert(root, 2)
root = insert(root, 20)
root = insert(root, 8)
print(all_paths(root,[]))
level(root,[])
'''

'''level order traversal count the no of leaf nodes'''
'''
class Node:
    def __init__(self, u):
        self.data = u
        self.left = None
        self.right = None

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

def search_in_tree(root, t):
    if root is None:
        return None
    if root.data == t:
        return root.data
    elif root.data > t:
        return search_in_tree(root.left, t)
    else:
        return search_in_tree(root.right, t)

def insert(root, x):
    if root is None:
        return Node(x)
    if x < root.data:
        root.left = insert(root.left, x)
    else:
        root.right = insert(root.right, x)
    return root
def all_paths(root,l):
    if(root==None):
        return 
    l.append(root.data)
    if(root.left==None and root.right==None):
        print(l)
        l.pop()
        return
    all_paths(root.left,l)
    all_paths(root.right,l)
    l.pop()
def level_count(root,l):
    if root==None:
        return
    l.append(root)
    c=0
    while(l):
        curr=l.pop(0)
        if(curr.left==None and curr.right==None):
            c=c+1
        if(curr.left!=None):
            l.append(curr.left)
        if(curr.right!=None):
            l.append(curr.right)
        print(curr.data,end=" ")
    print("\n",c)    
   
        
root = None
root = insert(root, 10)
root = insert(root, 5)
root = insert(root, 2)
root = insert(root, 20)
root = insert(root, 8)
#print(all_paths(root,[]))
level_count(root,[])
'''


'''print the left view
'''

'''
class Node:
    def __init__(self, u):
        self.data = u
        self.left = None
        self.right = None

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

def search_in_tree(root, t):
    if root is None:
        return None
    if root.data == t:
        return root.data
    elif root.data > t:
        return search_in_tree(root.left, t)
    else:
        return search_in_tree(root.right, t)

def insert(root, x):
    if root is None:
        return Node(x)
    if x < root.data:
        root.left = insert(root.left, x)
    else:
        root.right = insert(root.right, x)
    return root
def all_paths(root,l):
    if(root==None):
        return 
    l.append(root.data)
    if(root.left==None and root.right==None):
        print(l)
        l.pop()
        return
    all_paths(root.left,l)
    all_paths(root.right,l)
    l.pop()
def level_count(root,l):
    if root==None:
        return
    l.append(root)
    c=0
    while(l):
        curr=l.pop(0)
        if(curr.left==None and curr.right==None):
            c=c+1
        if(curr.left!=None):
            l.append(curr.left)
        if(curr.right!=None):
            l.append(curr.right)
        print(curr.data,end=" ")
    print("\n",c)    
def left_view(root,c):
    if(root==None):
        return
    if(c not in d):
        d[c]=root.data
    left_view(root.left,c+1)
    left_view(root.right,c+1)
    
        
    
root = None
root = insert(root, 10)
root = insert(root, 5)
root = insert(root, 2)
root = insert(root, 20)
root = insert(root, 8)
d={}
left_view(root,0)
print(d)
'''


'''right view'''
'''
class Node:
    def __init__(self, u):
        self.data = u
        self.left = None
        self.right = None

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

def search_in_tree(root, t):
    if root is None:
        return None
    if root.data == t:
        return root.data
    elif root.data > t:
        return search_in_tree(root.left, t)
    else:
        return search_in_tree(root.right, t)

def insert(root, x):
    if root is None:
        return Node(x)
    if x < root.data:
        root.left = insert(root.left, x)
    else:
        root.right = insert(root.right, x)
    return root
def all_paths(root,l):
    if(root==None):
        return 
    l.append(root.data)
    if(root.left==None and root.right==None):
        print(l)
        l.pop()
        return
    all_paths(root.left,l)
    all_paths(root.right,l)
    l.pop()
def level_count(root,l):
    if root==None:
        return
    l.append(root)
    c=0
    while(l):
        curr=l.pop(0)
        if(curr.left==None and curr.right==None):
            c=c+1
        if(curr.left!=None):
            l.append(curr.left)
        if(curr.right!=None):
            l.append(curr.right)
        print(curr.data,end=" ")
    print("\n",c)    
def right_view(root,c):
    if(root==None):
        return
    
    d[c]=root.data
    right_view(root.left,c+1)
    right_view(root.right,c+1)
    
        
    
root = None
root = insert(root, 10)
root = insert(root, 5)
root = insert(root, 2)
root = insert(root, 20)
root = insert(root, 8)
d={}
right_view(root,0)
print(d)
'''


'''top view'''
