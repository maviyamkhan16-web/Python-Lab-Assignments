def capitalize_lines(lines):
    for line in lines:
        print(line.upper())

# Example usage
print("Enter multiple lines (type 'END' to stop):")
lines = []
while True:
    line = input()
    if line.strip().upper() == "END":
        break
    lines.append(line)

capitalize_lines(lines)