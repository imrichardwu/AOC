class Solution:
    def p1(self, lines):
        # Split into top (number lines) and bottom (operator line)
        top_lines = [line.rstrip() for line in lines[:-1]]
        bottom_line = lines[-1].rstrip()
        
        # Count number of problems from first line
        num_problems = len(top_lines[0].split()) if top_lines else 0
        
        # Collect numbers for each problem
        nums = [[] for _ in range(num_problems)]
        for line in top_lines:
            for idx, s in enumerate(line.split()):
                nums[idx].append(int(s))
        
        # Extract operators from bottom line (filter out whitespace)
        ops = [c for c in bottom_line if c in ['+', '*']]
        
        # Calculate result
        res = 0
        for problem_nums, op in zip(nums, ops):
            if op == '+':
                total = sum(problem_nums)
            elif op == '*':
                total = 1
                for num in problem_nums:
                    total *= num
            res += total
        
        return res
    
    def main(self, lines):
        # Split into top (number lines) and bottom (operator line)
        top_lines = lines[:-1]
        bottom_line = lines[-1]
        
        # Find maximum width
        max_width = max(len(line.rstrip()) for line in top_lines)
        
        # Pad all lines to same width
        grid = []
        for line in top_lines:
            row = list(line.rstrip())
            while len(row) < max_width:
                row.append(' ')
            grid.append(row)
        
        ROWS = len(grid)
        COLS = max_width
        
        # Process columns from left to right
        problems = []
        curr = []
        
        for col in range(COLS):
            # Collect digits from top to bottom in this column
            digits = []
            for row in range(ROWS):
                char = grid[row][col]
                if char.isdigit():
                    digits.append(int(char))
            
            if digits:
                # Build number: acc * 10 + d for each digit (most significant at top)
                num = 0
                for d in digits:
                    num = num * 10 + d
                curr.append(num)
            else:
                # Empty column - end of problem
                if curr:
                    problems.append(curr)
                    curr = []
        
        # Don't forget the last problem
        if curr:
            problems.append(curr)
        
        # Extract operators from bottom line
        ops = [c for c in bottom_line if c in ['+', '*']]
        
        # Calculate result
        res = 0
        for problem, op in zip(problems, ops):
            if op == '+':
                total = sum(problem)
            elif op == '*':
                total = 1
                for num in problem:
                    total *= num
            res += total
        
        return res
                   
                

if __name__ == "__main__":
    sol = Solution()
    
    # Test with example
    example_lines = [
        "123 328  51 64 ",
        " 45 64  387 23 ",
        "  6 98  215 314",
        "*   +   *   +  "
    ]
    result = sol.p1(example_lines)

    with open("input.txt", "r") as file:
        lines = file.readlines()
        print(lines)
        result = sol.p1(lines)
        print(result)
