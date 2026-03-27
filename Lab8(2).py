# Step 1: Create a sample Python script with comments
with open("script.py", "w") as f:
    f.write("# This is a comment line\n")
    f.write("print('Hello World')\n")
    f.write("# Another comment\n")
    f.write("x = 10\n")
    f.write("y = 20\n")
    f.write("print(x + y)\n")

# Step 2: Copy contents without comments
with open("script.py", "r") as src, open("script_no_comments.py", "w") as dst:
    for line in src:
        if not line.strip().startswith("#"):  # skip comments
            dst.write(line)

print("✅ Python script copied successfully without comments!")

# Step 3: Print both files
print("\n--- Source File Content ---")
with open("script.py", "r") as src:
    print(src.read())

print("\n--- Destination File Content (No Comments) ---")
with open("script_no_comments.py", "r") as dst:
    print(dst.read())