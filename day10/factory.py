class Solution:
    def p1(self, lights, switches, joltages):
        
if __name__ == "__main__":
    sol = Solution()
    lights, switchs, joltages = [], [], []
    with open("input.txt", "r") as file:
        for line in file:
            # Extract the indicator pattern (remove brackets)
            start = line.find('[')
            end = line.find(']')
            pattern = line[start+1:end]
            lights.append(pattern)
            
            # Extract button schematics (find all parentheses groups)
            buttons = []
            i = end + 1
            while i < len(line):
                if line[i] == '(':
                    close = line.find(')', i)
                    button_str = line[i+1:close]
                    if button_str:  # if not empty
                        button_indices = [int(x) for x in button_str.split(',')]
                        buttons.append(button_indices)
                    i = close + 1
                elif line[i] == '{':
                    # Extract joltage requirements
                    close = line.find('}', i)
                    joltage_str = line[i+1:close]
                    joltage_values = [int(x) for x in joltage_str.split(',')]
                    joltages.append(joltage_values)
                    break
                else:
                    i += 1
            switchs.append(buttons)
    
    print(sol.p1(lights, switchs, joltages))