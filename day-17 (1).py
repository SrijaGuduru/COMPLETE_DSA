#day-17
#graphs
'''
graphs=[(5,2),(5,7),(5,8),(2,7),(2,8),(8,7),(8,3),(2,3)]
d={}
for i,j in graphs:
    if(i not in d):
        d[i]=[j]
    else:
        d[i].append(j)
    if(j not in d):
        d[j]=[i]
    else:
        d[j].append(i)
print(d)
'''



'''second classmethod'''
'''
import collections
graphs=[(5,2),(5,7),(5,8),(2,7),(2,8),(8,7),(8,3),(2,3)]
d=collections.defaultdict(list)
for i,j in graphs:
    d[i].append(j)
    d[j].append(i)
print(d)
'''



'''finding paths'''
'''
import collections
def print_all_paths(u,v,path=[]):
    path.append(u)
    if(u==v):
        print(path)
        path.pop()
        return 
    for i in d[u]:
        if(i not in path):
            print_all_paths(i,v,path)
    path.pop()
    return
graphs=[(5,2),(5,7),(5,8),(2,7),(2,8),(8,7),(8,3),(2,3)]
d=collections.defaultdict(list)
for i,j in graphs:
    d[i].append(j)
    d[j].append(i)
print(d)
print(print_all_paths(5,3))
'''


'''count of all paths'''
'''
import collections
def count_all_paths(u,v,path=[],c=0):
    path.append(u)
    if(u==v):
        c=c+1
    else:
       for i in d[u]:
           if(i not in path):
              c=count_all_paths(i,v,path,c)
    path.pop()
    return c
graphs=[(5,2),(5,7),(5,8),(2,7),(2,8),(8,7),(8,3),(2,3)]
d=collections.defaultdict(list)
for i,j in graphs:
    d[i].append(j)
    d[j].append(i)
print(d)
print(count_all_paths(5,3))
'''


'''check_if_path '''
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



