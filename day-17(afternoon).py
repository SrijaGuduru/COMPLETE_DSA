#day-17
'''check_if_path '''
'''
import collections
def check_if_path(u,v,path=[]):
    path.append(u)
    if(u==v):
        return True
    else:
       for i in d[u]:
           if(i not in path):
              if(check_if_path(i,v,path)):
                  return True
    path.pop()
    return False
graphs=[(5,2),(5,7),(5,8),(2,7),(2,8),(8,7),(8,3),(2,3)]
d=collections.defaultdict(list)
for i,j in graphs:
    d[i].append(j)
    d[j].append(i)
print(d)
print(check_if_path(5,3))
'''


'''using bfs to print all the nodes'''
'''
import collections
def check_if_path(u,v,path=[]):
    path.append(u)
    if(u==v):
        return True
    else:
       for i in d[u]:
           if(i not in path):
              if(check_if_path(i,v,path)):
                  return True
    path.pop()
    return False
def bfs_print_all_nodes(u):
    v={5}
    q=[u]
    while(q):
        curr=q.pop(0)
        print(curr)
        for i in d[curr]:
            if i not in v :
                v.add(i)
                q.append(i)
    print(v)
    
graphs=[(5,2),(5,7),(5,8),(2,7),(2,8),(8,7),(8,3),(2,3)]
d=collections.defaultdict(list)
for i,j in graphs:
    d[i].append(j)
    d[j].append(i)
print(d)
print(bfs_print_all_nodes(5))
'''

'''weighted graoh'''
'''
import collections
a=[(5,2,3),(5,7,2),(5,8,1),(2,7,2),(2,8,4),(8,7,1),(8,3,3),(2,3,2)]
d=collections.defaultdict(list)
for i,j,w in a:
    d[i].append([j,w])
    d[j].append([i,w])
print(d)
'''



'''all paths'''
'''
import collections
def print_all(u,v,path=[]):
    path.append(u)
    if(u==v):
        print(path)
    for i,w in d[u]:
        if(i not in path):
            print_all(i,v,path)
    path.pop()
    return
            
a=[(5,2,3),(5,7,2),(5,8,1),(2,7,2),(2,8,4),(8,7,1),(8,3,3),(2,3,2)]
d=collections.defaultdict(list)
for i,j,w in a:
    d[i].append([j,w])
    d[j].append([i,w])
print(d)
print(print_all(5,3))
'''


'''print weights'''
'''
import collections
def print_cost(u,v,path=[],cost=0):
    path.append(u)
    if(u==v):
        print(path,cost)
    for i,w in d[u]:
        if(i not in path):
            cost=cost+w
            print_cost(i,v,path,cost)
            cost=cost-w
    path.pop()
    return
        
a=[(5,2,3),(5,7,2),(5,8,1),(2,7,2),(2,8,4),(8,7,1),(8,3,3),(2,3,2)]
d=collections.defaultdict(list)
for i,j,w in a:
    d[i].append([j,w])
    d[j].append([i,w])
print(d)
print(print_cost(5,3))
'''
