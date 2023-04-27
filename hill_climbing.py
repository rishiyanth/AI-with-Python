#AI7: Hill climbing

# Hill Climbing

def heuristic(n):
   
    return H_dist[n]

def  m_distance(src,goal):
    src_x, src_y = Graph_coordinates[src]
    goal_x,goal_y = Graph_coordinates[goal]
    
    return abs(src_x-goal_x)+ abs(src_y-goal_y)


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


    
def makeGraph():
    adj = dict()
    adj['A'] = [heuristic('E'),heuristic('H')]
    adj['E'] = [heuristic('A'),heuristic('B'),heuristic('I')]
    adj['H'] = [heuristic('A'),heuristic('O'),heuristic('I')]
    adj['B'] = [heuristic('C'),heuristic('E'),heuristic('I'),heuristic('K')]
    adj['C'] = [heuristic('B'),heuristic('D'),heuristic('F')]
    adj['I'] = [heuristic('B'),heuristic('E'),heuristic('H'),heuristic('L'),heuristic('J')]
    adj['K'] = [heuristic('B'),heuristic('F'),heuristic('J'),heuristic('Q'),heuristic('M')]
    adj['D'] = [heuristic('C'), heuristic('G')]
    adj['F'] = [heuristic('C'),heuristic('K')]
    adj['G'] = [heuristic('D'),heuristic('N')]
    adj['N'] = [heuristic('G'),heuristic('R'),heuristic('X')]
    adj['O'] = [heuristic('H'),heuristic('L'),heuristic('S')]
    adj['L'] = [heuristic('I'),heuristic('P'),heuristic('O')]
    adj['J'] = [heuristic('I'),heuristic('Q'),heuristic('K')]
    adj['Q'] = [heuristic('J'),heuristic('K'),heuristic('M'),heuristic('P')]
    adj['M'] = [heuristic('K'),heuristic('Q')]
    adj['P'] = [heuristic('L'),heuristic('Q'),heuristic('U')]
    adj['R'] = [heuristic('N'),heuristic('T'),heuristic('X')]
    adj['X'] = [heuristic('N'),heuristic('R'),heuristic('W')]
    adj['S'] = [heuristic('O'),heuristic('U')]
    adj['U'] = [heuristic('P'),heuristic('S'),heuristic('T'),heuristic('W')]
    adj['T'] = [heuristic('R'),heuristic('U'),heuristic('W')]
    adj['W'] = [heuristic('T'),heuristic('U'),heuristic('X')]

    return adj
    

def hill_climbing(adj, curr_node, curr_val, goal):
    global path
    path.append((curr_node, curr_val))    
    if(curr_node == goal):
        return    
    for node, value in adj[curr_node]:
        # print(node, " ",value)
        if(value < curr_val):
            curr_node = node
            curr_val = value
            break
    hill_climbing(adj, curr_node, curr_val, goal)
        

if __name__ == "__main__":
    src = 'P'
    goal = 'D'
    H_dist = {}
    print("Heuristics:")
    for node in  Graph_coordinates:
        H_dist[node] = (node,m_distance(src= node,goal = goal))
        print(H_dist[node])
    adj = makeGraph()
    # print("\nInput Graph : ", adj)
    starting_val = H_dist[src][1]
    print("\nStarting node = ", src)
    print("Goal node", goal)
    path = []
    hill_climbing(adj, src, starting_val,  goal)
    print("\nPath taken - ", path)