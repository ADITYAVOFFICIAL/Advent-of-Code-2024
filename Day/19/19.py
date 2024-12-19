def can_construct(design, patterns, memo):
    if design in memo:
        return memo[design]
    if not design:
        return True

    for pattern in patterns:
        if design.startswith(pattern):
            if can_construct(design[len(pattern):], patterns, memo):
                memo[design] = True
                return True

    memo[design] = False
    return False


def count_possible_designs(filename):
    with open(filename, 'r') as file:
        lines = file.read().strip().split('\n')

    # Split available patterns and desired designs
    patterns = lines[0].split(', ')
    designs = lines[2:]  # Skip the blank line

    # Use a set for faster lookup of patterns
    pattern_set = set(patterns)
    memo = {}
    
    count = 0
    for design in designs:
        if can_construct(design, pattern_set, memo):
            count += 1

    return count


# Filepath to input file
input_file = "./Inputs/19.txt"
result = count_possible_designs(input_file)
print("Number of possible designs:", result)
