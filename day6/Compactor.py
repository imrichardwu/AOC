class Solution:
    def p1(self, problems):
        res = 0
        for nums, operator in problems:
            if not nums:
                continue
            if operator == '+':
                total = sum(nums)
            elif operator == '*':
                total = 1
                for num in nums:
                    total *= num
            res += total
    
    def p2(self, problems):
        res = 0
        for nums, operator in problems:
            col = max(nums)
            # read num from right to left top to bottom
            if operator == '+':
                total = sum(nums)
            elif operator == '*':
                total = 1
                for num in nums:
                    total *= num
                    


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        lines = [line.rstrip() for line in file]
    
    # Find the maximum line length to handle all columns
    max_len = max(len(line) for line in lines)
    
    # Separate number lines from operator line
    num_lines = lines[:-1]  # All lines except the last
    op_line = lines[-1]      # Last line with operators
    
    # Find column boundaries (columns where all rows have spaces)
    separator_cols = []
    for col in range(max_len):
        # Check if this column is all spaces in all number lines
        is_separator = True
        for line in num_lines:
            if col < len(line) and line[col] != ' ':
                is_separator = False
                break
        if is_separator:
            separator_cols.append(col)
    
    # Group columns into problems
    # Problems are between separator columns
    problems = []
    start_col = 0
    
    for sep_col in separator_cols:
        if sep_col > start_col:
            # Extract numbers from this column range
            problem_nums = []
            for line in num_lines:
                # Extract all numbers from this column range
                segment = line[start_col:sep_col] if start_col < len(line) else ''
                # Split by spaces and extract numbers
                parts = segment.split()
                for part in parts:
                    try:
                        num = int(part)
                        problem_nums.append(num)
                    except ValueError:
                        pass
            
            # Get the operator for this problem
            # Find the operator in the operator line for this column range
            op_segment = op_line[start_col:sep_col] if start_col < len(op_line) else ''
            op = None
            for char in op_segment:
                if char in '+*':
                    op = char
                    break
            
            if problem_nums and op:
                problems.append((problem_nums, op))
        
        start_col = sep_col + 1
    
    # Handle the last problem (after the last separator)
    if start_col < max_len:
        problem_nums = []
        for line in num_lines:
            segment = line[start_col:] if start_col < len(line) else ''
            parts = segment.split()
            for part in parts:
                try:
                    num = int(part)
                    problem_nums.append(num)
                except ValueError:
                    pass
        
        op_segment = op_line[start_col:] if start_col < len(op_line) else ''
        op = None
        for char in op_segment:
            if char in '+*':
                op = char
                break
        
        if problem_nums and op:
            problems.append((problem_nums, op))
    
    sol = Solution()
    sol.p1(problems)