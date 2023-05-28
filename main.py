current_file_path = None
file_open = None
file_contents = None
file_contents_arr = None
line_number = None
choice = None 
stri = '''
'''

def main():
    global current_file_path, file_open, file_contents, line_number, stri
    current_file_path = str(input("Enter file path:- "))
    try:
        file_open = open(current_file_path, "r+")
        pass 
    except UnicodeDecodeError:
        print("invalid text file")
    except FileNotFoundError:
        print("file not found")

    file_contents = file_open.read()
    file_contents_arr = file_contents.splitlines()
    print("\nfile preview:- \n")
    for i in range(0, len(file_contents_arr)):
        print(i+1, file_contents_arr[i])

    while True:
        print("[s] save")
        print("[e] edit ")
        print("[x] exit")
        print("[v] view")
        choice = str(input("enter choice:- "))
        if choice == "x":
            break
        elif choice == "s":
            stri ='''
'''
            for i in range(0 , len(file_contents_arr)):
                if i == 0:
                    stri = stri+file_contents_arr[i]
                else:
                    stri = stri+"\n"+file_contents_arr[i]

            file_open.seek(0)
            file_open.write(stri)
            file_open.truncate()
            continue
        elif choice == "e":
            print("this file has", len(file_contents_arr), "lines")
            line_number = int(input("which line you want to edit? "))
            print('"',file_contents_arr[line_number-1],'"', "is the line you want to edit")
            new_line = str(input("enter new value:- "))
            file_contents_arr[line_number-1] = new_line
            continue

if __name__ == "__main__":
    print("welcome to ine")
    while True:
        print("[o] open a file")
        print("[e] exiting a file")
        choice = str(input("enter choice:- "))
        if choice == "o":
            main()
            break
        elif choice == "e":
            exit()
        else:
            print("invalid choice")
            continue
        
