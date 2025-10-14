# Prompt the user for filenames
source_file = input("Enter the name of the source file: ")
target_file = input("Enter the name of the target file: ")

try:
    # Open the source file for reading
    with open(source_file, 'r') as infile:
        contents = infile.read()

    # Open the target file for writing (creates or overwrites)
    with open(target_file, 'w') as outfile:
        outfile.write(contents)

    print(f"Contents of '{source_file}' have been copied to '{target_file}'.")

except FileNotFoundError:
    print(f"Error: The file '{source_file}' was not found.")
except PermissionError:
    print(f"Error: Permission denied when accessing one of the files.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
