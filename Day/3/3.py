import re

def extract_and_sum_mul_instructions(file_path):
    """
    Extracts valid mul instructions from the input string in a file and computes their sum.
    
    Parameters:
        file_path (str): Path to the file containing the corrupted memory string.
    
    Returns:
        int: Sum of the results of valid mul instructions.
    """
    # Read the input string from the file
    with open(file_path, 'r') as file:
        input_string = file.read()
    
    # Regular expression to match valid mul instructions
    pattern = r"mul\((\d+),(\d+)\)"
    
    # Find all matches
    matches = re.findall(pattern, input_string)
    
    # Calculate the sum of products
    total_sum = sum(int(x) * int(y) for x, y in matches)
    
    return total_sum

if __name__ == "__main__":
    # Path to the input file
    file_path = "./Inputs/3.txt"  # Replace with the path to your file
    
    # Compute the result
    result = extract_and_sum_mul_instructions(file_path)
    
    # Output the result
    print(f"The sum of the results of valid mul instructions is: {result}")
