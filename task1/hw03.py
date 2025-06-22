import sys
from pathlib import Path
from colorama import Fore,Style,init

init()

def print_directory_structure(path : Path , indent: str = ""):
    """
    displays the directory structure with color formatting.
    """
    if not path.exists():
        print(Fore.RED + f"Error: Path '{path}' does not exist."+ Style.RESET_ALL)
        return
    if not path.is_dir():
        print(Fore.RED + f"Error: Path '{path}' is not a directory."+Style.RESET_ALL)
        return
    
    print(Fore.BLUE + f"{path.name}/"+ Style.RESET_ALL)

    for item in sorted(path.iterdir()):
        if item.is_dir():
            print(indent + Fore.BLUE + f"{item.name}/" + Style.RESET_ALL)
            print_directory_structure(item, indent + "    ")
        else:
            print(indent + Fore.GREEN + f"{item.name}" + Style.RESET_ALL)

def main():
    if len(sys.argv) != 2:
        print(Fore.YELLOW + "Usage: python hw03.py <directory_path>" + Style.RESET_ALL)
        sys.exit(1)

    dir_path = Path(sys.argv[1])
    print_directory_structure(dir_path)

if __name__ == "__main__":
    main()

        

