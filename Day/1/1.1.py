# Read numbers from a text file and calculate similarity score

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

def calculate_similarity_score(left_list, right_list):
    """
    Calculates the similarity score based on the frequency of numbers in the right list.
    """
    # Count the frequency of each number in the right list
    from collections import Counter
    right_count = Counter(right_list)

    # Calculate the similarity score
    similarity_score = sum(num * right_count[num] for num in left_list)
    return similarity_score

if __name__ == "__main__":
    # Path to the text file
    file_path = "./Inputs/1.txt"  # Replace with your file path

    # Read numbers from the file
    left_list, right_list = read_numbers_from_file(file_path)

    # Calculate similarity score
    similarity_score = calculate_similarity_score(left_list, right_list)

    # Output the result
    print(f"The similarity score between the lists is: {similarity_score}")
