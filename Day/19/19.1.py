from collections import defaultdict

def count_ways(design, patterns, memo):
    if design in memo:
        return memo[design]
    if not design:
        return 1

    ways = 0
    for pattern in patterns:
        if design.startswith(pattern):
            ways += count_ways(design[len(pattern):], patterns, memo)

    memo[design] = ways
    return ways

def total_arrangements(filename):
    with open(filename, 'r') as file:
        lines = file.read().strip().split('\n')

    # Split available patterns and desired designs
    patterns = lines[0].split(', ')
    designs = lines[2:]  # Skip the blank line

    # Use a set for faster lookup of patterns
    pattern_set = set(patterns)
    total_ways = 0
    
    for design in designs:
        memo = {}
        total_ways += count_ways(design, pattern_set, memo)

    return total_ways

# Filepath to input file
input_file = "./Inputs/19.txt"
result = total_arrangements(input_file)
print("Total number of arrangements:", result)
