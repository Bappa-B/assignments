# Input string
input_string = "hello world! 123"

# Initialize counters
letters = digits = 0

# Count letters and digits
for char in input_string:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1

print(f"LETTERS {letters}")
print(f"DIGITS {digits}")
