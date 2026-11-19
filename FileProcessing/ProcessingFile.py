file = open("FileProcessing/data.txt", "r")
print("File opened successfully for reading!")

content = file.read()
print("Entire content:\n", content)

file = open("FileProcessing/data.txt", "r")
for line in file:
    print("Line from file:", line.strip())
file.close()

try:
    file = open("FileProcessing/data.txt", "r")
    print("File is opened and being processed.")
except FileNotFoundError:
    print("Error: The file was not found.")
finally:
    if 'file' in locals() and not file.closed:
        file.close()
        print("File has been closed")
