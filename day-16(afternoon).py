#day-16
#top view
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
def top_view(root):
    c=0
    l=[(root,c)]
    d={}
    while(l):
        curr,c=l.pop(0)
        if c not in d:
            d[c]=curr.data
        if(curr.left!=None):
            l.append((curr.left,c-1))
        if(curr.right!=None):
            l.append((curr.right,c+1))
    for i in sorted(d):
        print(d[i],end=" ")
        
    
root = None
root = insert(root, 10)
root = insert(root, 5)
root = insert(root, 2)
root = insert(root, 20)
root = insert(root, 8)
top_view(root)

'''


'''bottom view'''
#make changes
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
def bottom_view(root):
    c=0
    l=[(root,c)]
    d={}
    while(l):
        curr,c=l.pop(0)
       
        d[c]=curr.data
        if(curr.left!=None):
            l.append((curr.left,c-1))
        if(curr.right!=None):
            l.append((curr.right,c+1))
    for i in sorted(d):
        print(d[i],end=" ")
        
    
root = None
root = insert(root, 10)
root = insert(root, 5)
root = insert(root, 2)
root = insert(root, 20)
root = insert(root, 8)
bottom_view(root)
'''


'''ancestor '''
#lca(lowest common ancestor )
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
def top_view(root):
    c=0
    l=[(root,c)]
    d={}
    while(l):
        curr,c=l.pop(0)
        if c not in d:
            d[c]=curr.data
        if(curr.left!=None):
            l.append((curr.left,c-1))
        if(curr.right!=None):
            l.append((curr.right,c+1))
    for i in sorted(d):
        print(d[i],end=" ")
def lca_bst(root,p,q):
    if(root==None):
        return
    if(p<root.data and q<root.data):
        lca_bst(root.left,p,q)
    if(p>root.data and q>root.data):
        lca_bst(root.right,p,q)
    return root.data
        
    
root = None
root = insert(root, 10)
root = insert(root, 5)
root = insert(root, 2)
root = insert(root, 20)
root = insert(root, 8)
lca_bst(root,5,20)
print(root.data)
'''


'''check whether the tree is balanced or not'''
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
def height(root):
    if(root==None):
        return -1
    return max(height(root.left),height(root.right))
def bal_or_not(root):
    if(root==None):
        return True
    l=height(root.left)
    r=height(root.right)
    if(abs(l-r)>1):
        return False
    return bal_or_not(root.left) and bal_or_not(root.right)
    
    
root = None
root = insert(root, 10)
root = insert(root, 5)
root = insert(root, 2)
root = insert(root, 20)
root = insert(root, 8)
print(height(root))
print(bal_or_not(root))



