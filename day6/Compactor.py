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
        return res
    
    def p2(self, num_lines, op_line, max_len):
        # For Part 2, we read right-to-left, one column at a time
        # Each number is in its own column, with most significant digit at top, least at bottom
        # Read each column top-to-bottom to get the number
        
        # Find separator columns (columns that are all spaces in number lines)
        separator_cols = []
        for col in range(max_len):
            is_separator = True
            for line in num_lines:
                if col < len(line) and line[col] != ' ':
                    is_separator = False
                    break
            if is_separator:
                separator_cols.append(col)
        
        # Process problems from right to left
        problems = []
        
        # Add boundaries
        all_boundaries = [0] + separator_cols + [max_len]
        
        # Process each problem region from right to left
        for i in range(len(all_boundaries) - 1, 0, -1):
            end_col = all_boundaries[i]
            start_col = all_boundaries[i-1]
            
            if end_col <= start_col:
                continue
            
            # Extract numbers from this problem region
            # Read columns from right to left, each column is a number read top-to-bottom
            problem_nums = []
            
            for col in range(end_col - 1, start_col - 1, -1):
                # Read this column from top to bottom
                num_str = ''
                for line in num_lines:
                    if col < len(line) and line[col].isdigit():
                        num_str += line[col]
                    elif col < len(line) and line[col] != ' ':
                        # Non-digit, non-space character - might be part of formatting
                        pass
                
                # If we found digits in this column, it's a number
                if num_str:
                    try:
                        problem_nums.append(int(num_str))
                    except ValueError:
                        pass
            
            # Reverse to get numbers in left-to-right order (since we processed right-to-left)
            problem_nums = list(reversed(problem_nums))
            
            # Get the operator (rightmost operator in this region)
            op = None
            for col in range(end_col - 1, start_col - 1, -1):
                if col < len(op_line) and op_line[col] in '+*':
                    op = op_line[col]
                    break
            
            if problem_nums and op:
                problems.append((problem_nums, op))
        
        # Calculate total
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
        return res
        


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
    print("Part 1:", sol.p1(problems))
    print("Part 2:", sol.p2(num_lines, op_line, max_len))