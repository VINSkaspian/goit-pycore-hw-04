
def get_cats_info(path):
    """
    Reads a file with data about cats and returns a list of dictionaries with information about each cat.
    
    Args:
    path (str): Path to a text file, where each line contains the cat's id, name, and age.
    
    Returns:
    list: List of dictionaries with keys "id", "name", "age".
    """
    cats_list = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                parts = line.split(',')
                if len(parts) == 3:
                    cat_id, name, age = parts
                    cat_dict = {
                        "id": cat_id,
                        "name": name,
                        "age": age
                    }
                    cats_list.append(cat_dict)
                else:
                    print(f"Invalid line format: '{line}'. Skipping.")
    except FileNotFoundError:
        print(f"File not found at path: '{path}'")
        return []
    except Exception as e:
        print(f"An error occurred while reading file: {e}")
        return []

    return cats_list


cats_info = get_cats_info("cats.txt")
print(cats_info)

    
    