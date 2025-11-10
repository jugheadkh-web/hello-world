def main():
    filename = input("Enter the filename: ")
    
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("File not found.")
        return

    total_lines = len(lines)
    print(f"The file has {total_lines} lines.")

    while True:
        try:
            line_num = int(input(f"Enter a line number (1-{total_lines}, 0 to quit): "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue
        
        if line_num == 0:
            print("Exiting program.")
            break
        elif 1 <= line_num <= total_lines:
            print(f"Line {line_num}: {lines[line_num - 1].rstrip()}")
        else:
            print(f"Invalid line number. Enter a number between 1 and {total_lines}.")

if __name__ == "__main__":
    main()
