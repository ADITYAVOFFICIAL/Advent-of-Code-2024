def is_safe_report(report):
    """
    Determines if a report is safe. A report is safe if:
    1. All levels are strictly increasing or strictly decreasing.
    2. The difference between any two adjacent levels is at least 1 and at most 3.
    """
    diffs = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    
    # Check if differences are all positive or all negative
    is_increasing = all(1 <= diff <= 3 for diff in diffs)
    is_decreasing = all(-3 <= diff <= -1 for diff in diffs)
    
    return is_increasing or is_decreasing

def count_safe_reports(file_path):
    """
    Reads a file containing reports and counts how many are safe.
    Each line in the file contains a space-separated list of numbers.
    """
    safe_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            report = list(map(int, line.split()))
            if is_safe_report(report):
                safe_count += 1
    return safe_count

if __name__ == "__main__":
    # Path to the input file
    file_path = "./Inputs/2.txt"  # Replace with the path to your puzzle input

    # Count safe reports
    safe_reports = count_safe_reports(file_path)

    # Output the result
    print(f"The number of safe reports is: {safe_reports}")
