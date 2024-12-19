# Read numbers from a text file and calculate total distance

def read_numbers_from_file(file_path):
    """
    Reads two lists of numbers from a text file where each line contains two numbers separated by whitespace.
    """
    left_list = []
    right_list = []
    with open(file_path, 'r') as file:
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
    return left_list, right_list

def calculate_total_distance(left_list, right_list):
    """
    Calculates the total distance between the sorted pairs of two lists.
    """
    # Sort both lists
    left_list.sort()
    right_list.sort()

    # Calculate the total distance
    total_distance = sum(abs(l - r) for l, r in zip(left_list, right_list))
    return total_distance

if __name__ == "__main__":
    # Path to the text file
    file_path = "./Inputs/1.txt"  # Replace with your file path

    # Read numbers from the file
    left_list, right_list = read_numbers_from_file(file_path)

    # Calculate total distance
    total_distance = calculate_total_distance(left_list, right_list)

    # Output the result
    print(f"The total distance between the lists is: {total_distance}")