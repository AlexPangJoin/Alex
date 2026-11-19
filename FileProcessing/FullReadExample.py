file = None
try:
    file = open("sample.txt", "r")
    print("---Reading from sample.txt ---")
    for line in file:
        print(line.strip())
    print("---Finished Reading ---")

except FileNotFoundError:
    print("Error: The file'sample.txt' was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    if file is not None and not file.closed:
        file.close()
        print("File has been closed.")