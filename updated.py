import os

# Prompt the user for the source file name
source_file = input("Enter the name of the source file (include extension): ")

# Get the user's Desktop path (works on Windows, macOS, Linux)
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Prompt for the target filename only (it will be saved to Desktop)
target_filename = input("Enter the name for the new file (include extension): ")

# Full path for the destination file on the Desktop
target_file = os.path.join(desktop_path, target_filename)

try:
    # Read from source file
    with open(source_file, 'r') as infile:
        contents = infile.read()

    # Write to file on Desktop
    with open(target_file, 'w') as outfile:
        outfile.write(contents)

    print(f" Contents of '{source_file}' have been copied to '{target_file}'")

except FileNotFoundError:
    print(f" Error: The file '{source_file}' was not found.")
except PermissionError:
    print(f" Error: Permission denied when accessing one of the files.")
except Exception as e:
    print(f" An unexpected error occurred: {e}")
