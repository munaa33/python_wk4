try:
    file_name = input("Enter the file name to read: ")
    with open(file_name, 'r') as file:
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    print("Error: The file does not exist. Please check the file name and try again.")
except PermissionError:
    print("Error: You do not have permission to read this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")