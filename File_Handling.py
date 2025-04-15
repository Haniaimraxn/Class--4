# File Handling in Python
# it refers to the process of performing operations like creating, opening, reading, writing, appending and closing files using   built-in ffunctions. It allows programs to store data permanently, interact with external files, and manage input/output operations.

# Example:
# 'r'- Read (default mode)
# 'w'- Write (creates a new file or overwrites)
# 'a'-Append (adds data to the end)
# 'x'-Create (create file, fails if it exits)

# Writing to a file

try:
    file = open("example.txt", "w")  # 'w' means write mode
    file.write("Hello, this is a sample text.\nWelcome to Python file handling!")
except Exception as e:
    print("An error occurred while writing to the file:", e)
else:
    print("File written successfully.")
finally:
    file.close()
    print("File is closed after writing.")

# Reading from the same file
try:
    file = open("example.txt", "r")  # 'r' means read mode
    content = file.read()
except Exception as e:
    print("An error occurred while reading the file:", e)
else:
    print("File content:\n", content)
finally:
    file.close()
    print("File is closed after reading.")

    with open("data.txt", "w") as file:
        file.write("This is file handling in Python.")