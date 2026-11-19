file = None
try:
    file = open("output.txt", "w")
    print("File opened for writing.")

except IOError as e:
    print(f"Error opening file for writing: {e}")

file = open("output.txt", "w")
file.write("Hello, World!\n")
file.write("This is a second line.\n")
file.close()

file = open("output.txt", "a")
file.write("This line was appended to the end.\n")
file.close()