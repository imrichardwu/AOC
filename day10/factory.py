from collections import deque

class Solution:
    def p1(self, lights, button, jolts):
        goal = 0
        for i, light in enumerate(lights):
            if light == 1:
                goal |= (1 << i)

        # Precompute button masks for efficiency
        masks = []
        for group in button:
            mask = 0
            # Create a bitmask for each button group
            for i in group:
                mask |= (1 << i) # Set the i-th bit
            masks.append(mask)

        queue = deque([(0, 0)])  # (current_state, steps)
        seen = set([0])
        
        # BFS to find the minimum button presses
        while queue:
            current, steps = queue.popleft() # current state and number of steps

            if current == goal:
                return steps   

            for mask in masks:
                next_state = current ^ mask # Toggle the bits using XOR
                if next_state not in seen:
                    seen.add(next_state)
                    queue.append((next_state, steps + 1))

        return 0

if __name__ == "__main__":
    solution = Solution()
    total_presses = 0
    
    with open("input.txt", "r") as file:
        for line in file:
            lightStr, rest = line.strip().split(" ", 1)
            buttonStr, joltStr = rest.rsplit(" ", 1)

            lights = []
            for char in lightStr:
                if char == "#":
                    lights.append(1)
                elif char == ".":
                    lights.append(0)

            buttons = []
            for group in buttonStr.split():
                group = group.strip("()")
                if group:
                    nums = [int(num) for num in group.split(",")]
                    buttons.append(nums)

            jolts = []
            for jolt in joltStr.strip('{}').split(","):
                jolts.append(int(jolt))

            presses = solution.p1(lights, buttons, jolts)
            total_presses += presses

    print(total_presses)