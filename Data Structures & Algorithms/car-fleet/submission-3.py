class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        #function takes 3 args, an int, a list int, a list int
        #proccess at what time the car reaches the destination,
        #the first list is position of each cars, and second list of the speed they are going
        #when target - po[i] = remaining miles
        #when remaining miles / speed[i] = remaining hrs
        

        #create a set
        #iterate to each lists, sub position from target and divide it by speed
        #add it to the set

        cars = sorted(zip(position, speed), reverse=True)  # sort by position descending
        stack = []

        for pos, spd in cars:
            time = (target - pos) / spd
            if not stack or time > stack[-1]:
                stack.append(time)  # New fleet
            # else: same fleet, do nothing

        return len(stack)