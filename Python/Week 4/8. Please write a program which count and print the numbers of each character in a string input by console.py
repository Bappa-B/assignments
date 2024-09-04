# Input string
input_string = "abcdefgabc"

# Dictionary to store character counts
char_count = {}

# Count each character
for char in input_string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# Print the results
for char, count in sorted(char_count.items()):
    print(f"{char},{count}")
