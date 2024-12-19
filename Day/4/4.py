def count_xmas_in_grid(file_path):
    """
    Counts occurrences of the word 'XMAS' in a grid considering all possible directions.

    Parameters:
        file_path (str): Path to the file containing the grid.

    Returns:
        int: Total count of 'XMAS' occurrences.
    """
    # Read the grid from the file
    with open(file_path, 'r') as file:
        grid = [line.strip() for line in file.readlines()]

    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    word = "XMAS"
    word_length = len(word)
    directions = [
        (0, 1),    # Right
        (1, 0),    # Down
        (0, -1),   # Left
        (-1, 0),   # Up
        (1, 1),    # Down-Right
        (1, -1),   # Down-Left
        (-1, 1),   # Up-Right
        (-1, -1)   # Up-Left
    ]

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def count_word_from(x, y, dx, dy):
        for i in range(word_length):
            nx, ny = x + i * dx, y + i * dy
            if not is_valid(nx, ny) or grid[nx][ny] != word[i]:
                return 0
        return 1

    total_count = 0

    for r in range(rows):
        for c in range(cols):
            for dx, dy in directions:
                total_count += count_word_from(r, c, dx, dy)

    return total_count


if __name__ == "__main__":
    # Path to the input file
    file_path = "./Inputs/4.txt"  # Replace with the path to your input file

    # Count occurrences of 'XMAS' and print the result
    result = count_xmas_in_grid(file_path)
    print(result)
