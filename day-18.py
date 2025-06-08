#day-18
#dijkstras algorithm
'''give shorest path with cost
print shorest path from 10 to 3'''

'''
import collections 
def sssp(u,v):
    dis=collections.defaultdict(lambda : float('inf'))
    sp=collections.defaultdict(int)
    sp[u]=u
    dis[u]=0
    q=[u]
    vi=set()
    while(q):
        n=q.pop()
        vi.add(n)
        for i,w in d[n]:
            if(dis[n]+w<dis[i]):
                dis[i]=dis[n]+w
                sp[i]=n
            if(i not in q and i not in vi):
                q.append(i)
    print(dis)
a=[(10,5,2),(10,7,4),(5,10,2),(5,8,3),(5,7,1),(5,3,2),(8,5,3),(8,7,1),(8,3,1),(3,5,2),(3,8,1)]
d=collections.defaultdict(list)
for i,j,w in a:
    d[i].append([j,w])
    d[j].append([i,w])
print(d)
print(sssp(10,3))
 '''
 
 
 
#prims algorrithm
#use bfs for prims algorithm
#cost of minimum spanning tree
'''
import collections

def prims(start):
    visited = set()
    mst_weight = 0
    q = [start]
    edges = []

    while q:
        node = q.pop(0)
        if node in visited:
            continue
        visited.add(node)

        for neighbor, weight in d[node]:
            if neighbor not in visited:
                edges.append((weight, node, neighbor))

        
        edges = sorted(edges)  
        while edges:
            w, u, v = edges.pop(0)
            if v not in visited:
                mst_weight += w
                q.append(v)
                break  
    print(mst_weight)

a = [(10, 5, 2), (10, 7, 4), (5, 8, 3), (5, 7, 1),
     (5, 3, 2), (8, 7, 1), (8, 3, 1)]

d = collections.defaultdict(list)
for u, v, w in a:
    d[u].append((v, w))
    d[v].append((u, w))
prims(3)
'''


#second classmethod
import collections
import heapq
def mst_prims(u):
    vi=set()
    mh=[(0,u)]
    mc=0
    while(mh):
        w,n=heapq.heappop(mh)
        if n in vi:
            continue
        vi.add(n)
        mc=mc+w
        for i,we in d[n]:
            if i not in vi:
                heapq.heappush(mh,(we,i))
    print(mc)
a = [(10, 5, 2), (10, 7, 4), (5, 8, 3), (5, 7, 1),
     (5, 3, 2), (8, 7, 1), (8, 3, 1)]

d = collections.defaultdict(list)
for u, v, w in a:
    d[u].append((v, w))
    d[v].append((u, w))
mst_prims(5)


