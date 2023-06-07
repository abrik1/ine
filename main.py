import os

# Global variables
current_file_path = None
file_open = None
file_contents_arr = None

# ANSI color codes
COLORS = {
    'yellow': '\033[93m',  # Options
    'red': '\033[91m',  # Error messages
    'reset': '\033[0m'  # Reset color
}

def clear_console():
    """Clears the console"""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def open_file():
    """
    Prompts user for file path and opens the file for editing.
    """
    global current_file_path, file_open, file_contents_arr
    current_file_path = str(input("\nEnter file path: "))
    try:
        file_open = open(current_file_path, "r+")
    except (UnicodeDecodeError, FileNotFoundError):
        print_error("Unable to open file. Please ensure the file path is correct and the file is a text file.")
        return False

    file_contents_arr = file_open.read().splitlines()
    return True

def close_file():
    """Closes the current file"""
    global file_open
    file_open.close()

def save_file():
    """
    Saves the current contents of the file.
    """
    global file_open, file_contents_arr
    file_open.seek(0)
    file_open.write("\n".join(file_contents_arr))
    file_open.truncate()

def preview_file():
    """
    Prints the current contents of the file.
    """
    global file_contents_arr
    for i, line in enumerate(file_contents_arr, start=1):
        print(f"{i} {line}")

def add_line():
    """
    Adds a new line to the end of the file.
    """
    global file_contents_arr
    file_contents_arr.append(str(input("Enter new line: ")))

def insert_line():
    """
    Inserts a new line at a specified line number in the file.
    """
    global file_contents_arr
    try:
        line_number = int(input("Enter line number to insert at: "))
        if line_number < 1 or line_number > len(file_contents_arr) + 1:
            print_error("Invalid line number.")
            return
        new_line = str(input("Enter new line: "))
        file_contents_arr.insert(line_number - 1, new_line)
    except ValueError:
        print_error("Invalid input. Please enter a line number.")

def edit_line():
    """
    Prompts user for line number and new line content,
    then replaces specified line with new content.
    """
    global file_contents_arr
    try:
        line_number = int(input("Enter line number to edit: "))
        if line_number < 1 or line_number > len(file_contents_arr):
            print_error("Invalid line number.")
            return
        file_contents_arr[line_number-1] = str(input("Enter new line: "))
    except ValueError:
        print_error("Invalid input. Please enter a line number.")

def delete_line():
    """
    Prompts user for a line or range of lines to delete, then deletes those lines.
    """
    global file_contents_arr
    try:
        line_range = input("Enter line or range to delete (e.g. 1 or [1:3]): ")
        if ":" in line_range:  # If input is a range of lines
            start, end = (int(x) for x in line_range.strip("[]").split(":"))
            if start < 1 or end > len(file_contents_arr) or start > end:
                print_error("Invalid range.")
                return
            del file_contents_arr[start-1:end]
        else:  # If input is a single line
            line_number = int(line_range)
            if line_number < 1 or line_number > len(file_contents_arr):
                print_error("Invalid line number.")
                return
            del file_contents_arr[line_number-1]
    except (ValueError, IndexError):
        print_error("Invalid input. Please enter a line number or range of lines.")

def print_error(message):
    """
    Prints the error message and logs it to the error log file.
    """
    global current_file_path
    print(f"{COLORS['red']}{message}{COLORS['reset']}")
    if current_file_path is not None:
        with open(f"{current_file_path.rsplit('.', 1)[0]}_err.log", 'a') as err_file:
            err_file.write(f"{message}\n")

def main():
    """
    Main loop of the text editor.
    """
    global file_contents_arr
    if not open_file():
        return
    while True:
        clear_console()
        preview_file()
        print(f"\n{COLORS['yellow']}[a] Add [i] Insert [e] Edit [s] Save [d] Delete [x] Exit{COLORS['reset']}")
        choice = input("Enter choice: ")
        if choice == "x":
            break
        elif choice == "s":
            save_file()
        elif choice == "e":
            edit_line()
        elif choice == "a":
            add_line()
        elif choice == "i":
            insert_line()
        elif choice == "d":
            delete_line()

if __name__ == "__main__":
    print("Welcome to ine")
    while True:
        print(f"\n{COLORS['yellow']}[o] Open a file [e] Exit{COLORS['reset']}")
        choice = input("Enter choice: ")
        if choice == "o":
            main()
            close_file()
            break
        elif choice == "e":
            exit()
        else:
            print_error("Invalid choice.")

