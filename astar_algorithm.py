from queue import PriorityQueue

def aStarAlgo(src,goal):
    pq = PriorityQueue()
    pq.put((src,0))
    parent = {}
    cost_so_far = {}
    parent[src] = None
    cost_so_far[src] = 0

    while not pq.empty():
        node,hcost = pq.get()

        if node== goal:
            break

        for neighbor,cost in Graph_nodes[node]:
            new_cost = cost_so_far[node] + cost + hcost
            if neighbor not in cost_so_far or new_cost< cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost - hcost
                prioritycost = new_cost + heuristic(neighbor) 
                pq.put((neighbor,prioritycost)) 
                parent[neighbor] = node

    return parent, cost_so_far


def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None
    
def heuristic(n):
   
    return H_dist[n]

def  m_distance(src,goal):
    src_x, src_y = Graph_coordinates[src]
    goal_x,goal_y = Graph_coordinates[goal]
    
    return abs(src_x-goal_x)+ abs(src_y-goal_y)

Graph_nodes = {
            'A': [('E', 25), ('H', 25)], 
            'E': [('A', 25), ('B', 33), ('I', 40)], 
            'H': [('A', 25), ('O', 25), ('I', 25)], 
            'B': [('C', 11), ('E', 33), ('I', 31), ('K', 33)], 
            'C': [('B', 11), ('D', 31), ('F', 24)], 
            'I': [('B', 31), ('E', 40), ('H', 25), ('L', 21), ('J', 21)], 
            'K': [('B', 33), ('F', 23), ('J', 22), ('Q', 32), ('M', 33)], 
            'D': [('C', 31), ('G', 25)], 
            'F': [('C', 24), ('K', 23)], 
            'G': [('D', 25), ('N', 33)], 
            'N': [('G', 33), ('R', 25), ('X', 45)], 
            'O': [('H', 25), ('L', 25), ('S', 28)], 
            'L': [('I', 21), ('P', 21), ('O', 25)], 
            'J': [('I', 21), ('Q', 11), ('K', 22)], 
            'Q': [('J', 11), ('K', 32), ('M', 43), ('P', 13)], 
            'M': [('K', 33), ('Q', 43)], 
            'P': [('L', 21), ('Q', 13), ('U', 25)], 
            'R': [('N', 25), ('T', 35), ('X', 45)], 
            'X': [('N', 45), ('R', 45), ('W', 25)], 
            'S': [('O', 28), ('U', 21)], 
            'U': [('P', 25), ('S', 21), ('T', 35), ('W', 42)], 
            'T': [('R', 35), ('U', 35), ('W', 35)], 
            'W': [('T', 35), ('U', 42), ('X', 25)]
            }

Graph_coordinates = {
    'A': [0,60],
    'B': [30,60],
    'C': [40,60],
    'D': [70,60],
    'E': [10,50],
    'F': [50,50],
    'G': [80,50],
    'H': [0,40],
    'I': [20,40],
    'J': [30,30],
    'K': [40,40],
    'L': [10,40],
    'M': [60,30],
    'N': [70,30],
    'O': [0,20],
    'P': [20,20],
    'Q': [30,20],
    'R': [60,20],
    'S': [10,10],
    'T': [40,10],
    'U': [20,0],
    'W': [60,0],
    'X': [80,0],
}

src = 'P'
goal = 'D'
H_dist = {}
solution = []
print("Heuristics:")
for node in  Graph_coordinates:
    H_dist[node] = m_distance(src= node,goal = goal)
    print(node, ' ', H_dist[node])

path,cost = aStarAlgo(src, goal)
totalcost = 0
parent = goal
solution.append(goal)
while parent!=None:
    solution.append(path[parent])
    parent = path[parent]

solution.reverse()
print("Solution:",solution)
print("Cost:",cost)