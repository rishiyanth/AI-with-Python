from collections import defaultdict as dd
import heapq
from queue import PriorityQueue

graph = dd(list)

visited = []

#for BFS
queue = []

#for DFS
stack = []

#for UCS
traversalpath = []

#for IDS
path = []

totalcost = 0

def addEdge(u,v,cost):
    graph[u].append((v,cost))

def BFS(src,goal):
    visited.append(src)
    queue.append(src)

    while queue:
        node = queue.pop(0)
        print(node)

        if(node == goal):
            break

        for child, cost in graph[node]:
            if child not in visited:
                visited.append(child)
                queue.append(child)
                global totalcost 
                totalcost += cost

    print("Solution cost:", totalcost)
    visited = []
    queue = []
    totalcost = 0

def DFS(src,goal):
    stack.append(src)
    visited.append(src)

    while stack:
        node = stack.pop()

        if(node == goal):
            print(node)
            global totalcost
            print("Total cost:",totalcost)

        for child,cost in graph[node]:
            if child not in visited:
                visited.append(child)
                # global totalcost
                print(visited,end="\n")
                totalcost += cost
                DFS(node,goal)

def UCS(src,goal):
    heap = [(0,src,[])]

    while heap:
        cost, node, path = heapq.heappop(heap)
        if node not in visited:
            path = path + [node]
            traversalpath.append(node)
            if node == goal:
                return cost,path
            
            for neighbor,weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(heap,(weight+cost,neighbor,path))
        print(traversalpath)
        
            
    return float("inf"),[]


def DLS(src, goal, maxDepth):
    traversalpath.append(src)
    
    if src == goal:
        return True

    if maxDepth <=0:
        return False
    
    for node, weight in graph[src]:
        if DLS(node,goal,maxDepth-1):
            path.append(node)
            global totalcost
            totalcost += weight
        return True

    return False

def IDS(src,goal,maxDepth):
    for i in range(maxDepth):
        if(DLS(src,goal,maxDepth)):
            return True
    
    return False

def GBFS(src,goal):
    visited.append(src)

    pq = PriorityQueue()
    pq.put((0,src))

    while pq.empty()==False:

        node = pq.get()[1]
        print(node,end=' ')
        if node==goal:
            break

        for neighbor,weight in graph[node]:
            if neighbor not in visited:
                visited.append(neighbor)
                global totalcost
                totalcost += weight
                pq.put((weight,neighbor))


addEdge('A','B',4)
addEdge('A','C',3)
addEdge('B','D',2)
addEdge('C','D',1)
addEdge('C','H',1)
addEdge('D','E',5)
addEdge('E','G',1)
addEdge('F','G',2)
addEdge('D','F',2)

start = 'A'
goal = 'G'

# print("DEPTH FIRST SEARCH")
# DFS(start,goal)

# print("BREADTH FIRST SEARCH")
# BFS(start,goal)

# print("UNIFORM COST SEARCH")
# cost, path = UCS(start,goal)
# print("Cost:",cost)
# print("Path",path)

# print("ITERATIVE DEEPENING SEARCH")
# IDS(start,goal,4)
# path.append(start)
# path.reverse()
# print("Path:")
# print(path)
# print("Solution Cost : ")
# print(totalcost)

print("GREEDY BEST FIRST SEARCH")
GBFS(start,goal)
print("\nTotal cost",totalcost)