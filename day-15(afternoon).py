#DAY-15
#tress

'''ip:[4,1,2]
      [2,1,3,4]
 op:[-1,3,3]
 next greater element(stack)
 '''

#creating binary tree
'''
class node:
    def __init__(self,u):
        self.data=u
        self.left=None
        self.right=None
root=node(10)
root.left=node(5)
root.right=node(20)
root.left.left=node(2)
root.left.right=node(8)
'''


'''in-order traversal'''
'''
class node:
    def __init__(self,u):
        self.data=u
        self.left=None
        self.right=None
    def inorder(self,root):
        if(root==None):
            return
        self.inorder(root.left)
        print(root.data,end=" ")
        self.inorder(root.right)
        
root=node(10)
root.left=node(5)
root.right=node(20)
root.left.left=node(2)
root.left.right=node(8)
root.inorder(root)
'''

#postorder
'''
class node:
    def __init__(self,u):
        self.data=u
        self.left=None
        self.right=None
    def inorder(self,root):
        if(root==None):
            return
        self.inorder(root.left)
        
        self.inorder(root.right)
        print(root.data,end=" ")
root=node(10)
root.left=node(5)
root.right=node(20)
root.left.left=node(2)
root.left.right=node(8)
root.inorder(root)
'''


#preorder
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
        
root=node(10)
root.left=node(5)
root.right=node(20)
root.left.left=node(2)
root.left.right=node(8)
root.inorder(root)
'''


'''write function to sum of all nodes(using functional recursion'''
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
    def sum_all_nodes(self,root):
        if root == None:
            return 0
        return root.data+self.sum_all_nodes(root.left)+self.sum_all_nodes(root.right)
root=node(10)
root.left=node(5)
root.right=node(20)
root.left.left=node(2)
root.left.right=node(8)

print(root.sum_all_nodes(root))
'''


'''write sum evens'''
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
    def sum_all_even_nodes(self,root):
        if root == None:
            return 0
        if root.data % 2 == 0:
            return root.data + self.sum_all_even_nodes(root.left)+self.sum_all_even_nodes(root.right)
        else:
            return self.sum_all_even_nodes(root.left)+self.sum_all_even_nodes(root.right)
        
root=node(10)
root.left=node(5)
root.right=node(20)
root.left.left=node(2)
root.left.right=node(8)
root.inorder(root)
print(root.sum_all_even_nodes(root))
'''

'''height'''
def height(self,root):
        if root == None:
            return -1
        return max(self.height(root.left),self.height(root.right))+1

