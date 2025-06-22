

def total_salary(path):
    """
    Parses a text file with developer salaries and calculates
    the total and average salary.
    
    Args:
        path (str): Path to the txt file containing salary data.
        Each line has the format "LastNameFirstName,salary".
    
    Returns:
        tuple: A tuple of two numbers:
        (total_salary, average_salary).
        Returns (0, 0) in case of file error or if the file is empty/does not contain valid data.
    """
    total_sum = 0
    developer_count = 0  # ✅ виправлено назву змінної

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                stripped_line = line.strip()
                if not stripped_line:
                    continue
                parts = stripped_line.split(',')
                if len(parts) == 2:
                    try:
                        salary = int(parts[1])
                        total_sum += salary
                        developer_count += 1
                    except ValueError:
                        print(f"Incorrect salary format in line: '{stripped_line}'. Skipping.")
                else:
                    print(f"Invalid line format: '{stripped_line}'. Skipping.")
    except FileNotFoundError:
        print(f"File not found at path '{path}'.")
        return 0, 0
    except Exception as e:
        print(f"An unknown error occurred while reading file '{path}': {e}")
        return 0, 0

    average_salary = total_sum / developer_count if developer_count > 0 else 0
    return total_sum, average_salary
total, average = total_salary("salaries.txt")
print(total, average)