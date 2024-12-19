import re

def extract_and_sum_with_conditions(file_path):
    """
    Extracts valid mul instructions based on conditional do() and don't() statements
    and computes their sum.

    Parameters:
        file_path (str): Path to the file containing the corrupted memory string.

    Returns:
        int: Sum of the results of valid and enabled mul instructions.
    """
    # Read the input string from the file
    with open(file_path, 'r') as file:
        input_string = file.read()

    # Regular expressions to match instructions
    mul_pattern = r"mul\((\d+),(\d+)\)"
    control_pattern = r"(do\(\)|don't\(\))"

    # Find all matches for mul and control instructions
    mul_matches = list(re.finditer(mul_pattern, input_string))
    control_matches = list(re.finditer(control_pattern, input_string))

    # Merge both types of matches into a single list and sort by position
    all_matches = mul_matches + control_matches
    all_matches.sort(key=lambda match: match.start())

    # Process the instructions
    mul_enabled = True  # Initially, mul instructions are enabled
    total_sum = 0

    for match in all_matches:
        if match.re.pattern == mul_pattern:
            # Handle mul instructions
            if mul_enabled:
                x, y = map(int, match.groups())
                total_sum += x * y
        elif match.re.pattern == control_pattern:
            # Handle do() or don't() instructions
            instruction = match.group()
            if instruction == "do()":
                mul_enabled = True
            elif instruction == "don't()":
                mul_enabled = False

    return total_sum


if __name__ == "__main__":
    # Path to the input file
    file_path = "./Inputs/3.txt"  # Replace with the path to your file

    # Compute the result
    result = extract_and_sum_with_conditions(file_path)

    # Output the result
    print(f"The sum of the results of enabled mul instructions is: {result}")
