file = open("data.txt", "r")
print("File opened successfully for reading!")

content = file.read()
print("Entire content:\n", content)

# file = open("data.txt", "r")
for line in file:
    print("Line from file:", line.strip())
file.close()