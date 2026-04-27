# Writing to a text file
with open("sample.txt", "w") as file:
    file.write("Hello, this is a sample file.\n")
    file.write("Python File Handling Example.\n")

# Reading the file
with open("sample.txt", "r") as file:
    content = file.read()
    print("File Content:")
    print(content)

# Appending data
with open("sample.txt", "a") as file:
    file.write("This line was appended later.\n")

# Reading updated content
with open("sample.txt", "r") as file:
    print("Updated File Content:")
    print(file.read())
