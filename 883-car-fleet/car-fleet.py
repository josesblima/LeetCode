class Solution:
    def carFleet(self, target: int, position, speed) -> int:
        sortstack = [None] * target
        # Counting sort
        for x in range(len(position)):
            sortstack[position[x]] = speed[x]
        posstack = []
        speedstack = []
        # Make 2 new position and speed variables
        for x in range(len(sortstack)):
            if sortstack[x] != None:
                posstack.append(x)
                speedstack.append(sortstack[x])
        arrivestack = [(target - posstack[0]) / speedstack[0]]
        # Slow down the cars that are behind when needed
        for x in range(1, len(posstack)):
            counter = 1
            while (target - posstack[x]) / speedstack[x] > arrivestack[x - counter]:
                arrivestack[x - counter] = (target - posstack[x]) / speedstack[x]
                counter += 1
            arrivestack.append((target - posstack[x]) / speedstack[x])
        prevarr = arrivestack[0]
        res = 1
        # Count the result
        for x in range(1, len(arrivestack)):
            if arrivestack[x] != prevarr:
                res += 1
                prevarr = arrivestack[x]
        return res

                


    carFleet(1, target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3])