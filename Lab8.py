# Step 1: Create a sample text file
with open("sample.txt", "w") as f:
    f.write("Hello, this is a sample file.\nIt contains multiple lines.\nPython file handling is fun!")

# Step 2: Read the file and write contents in uppercase to another file
with open("sample.txt", "r") as src:
    content = src.read()

with open("uppercase.txt", "w") as dst:
    dst.write(content.upper())

print("✅ Files created successfully!")
print("\n--- Original File Content ---")
print(content)
print("\n--- Uppercase File Content ---")
print(content.upper())