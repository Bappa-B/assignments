# Input string
input_string = "hello world and practice makes perfect and hello world again"

# Split the input string into a list of words
words = input_string.split()

# Remove duplicates by converting to a set, then sort the set
unique_sorted_words = sorted(set(words))

# Join the sorted list into a string
result = ' '.join(unique_sorted_words)
print(result)
