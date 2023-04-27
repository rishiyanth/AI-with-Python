#AI1: BFS - WaterJug 

class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if x > y:
            temp = x;
            x = y;
            y = temp;
            
        # if z > x + y:
        #     return False;
        
        # set the initial state will empty jars;
        queue = [(0, 0)];
        visited = set((0, 0));
        while len(queue) > 0:
            a, b = queue.pop(0);
            print(a,b) 
            if (a,b) == z:
                return True;
            
            states = set()
            
            states.add((x, b)) # fill jar x;
            states.add((a, y)) # fill jar y;
            states.add((0, b)) # empty jar x;
            states.add((a, 0)) # empty jar y;
            states.add( (min(x, b + a), 0 if b < x - a else b - (x - a))) # pour jar y to x;
            states.add((0 if a + b < y else a - (y - b), min(b + a, y))) # pour jar x to y;
            # print(states)
            for state in states:
                # print(state)
                if state in visited:
                    continue;
                queue.append(state)
                visited.add(state);
                
        return False;

aa = Solution()
print(aa.canMeasureWater(3,4,(3,4)))
# a = 1
# b = 5
# x = 10

# print(0 if b < x - a else b - (x - a))

class ThreeWaterJug(object):
    def solve(self,x,y,z,goal):
        queue = [(0,0,7)]
        visited = set((0,0,7))
        while len(queue) > 0:
            a,b,c = queue.pop(0)
            # print(a,b,c)
            if (a,b,c) == goal:
                return True
            states = set()
            # states.add((x,b,c))
            # states.add((a,y,c))
            # states.add((a,b,z))
            if a+c < x: #pour from 3 to 1
                states.add((a+c,b,0)) # pour from 3 to 1
            else:
                states.add((x,b,(c-(x-a))))
            
            if a+c < z: #pour from 1 to 3
                states.add((0,b,a+c))
            else:
                states.add((a-(z-c),b,z))
            
            if a+b < y: #pour from 1 to 2
                states.add((0,a+b,c))
            else:
                states.add((a-(y-b),y,c))
            
            if a+b < x : #pur from 2 to 1
                states.add(((a+b),0,c))
            else:
                states.add((x,b-(x-a),c))
            
            if b+c < z: #pour from 2 to 3
                states.add((a,0,(b+c)))
            else:
                states.add((a,b-(z-c),z))
            
            if b+c < y:
                states.add((a,b+c,0))
            else:
                states.add((a,y,(c-(y-b))))
            
            print(states)
            for state in states:
                if state in visited:
                    continue
                queue.append(state)
                visited.add(state)
        return False


bb = ThreeWaterJug()
bb.solve(2,5,7,(1,5,1))