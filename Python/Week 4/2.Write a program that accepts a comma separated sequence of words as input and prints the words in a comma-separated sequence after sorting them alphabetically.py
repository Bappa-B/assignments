# Input string
input_string = "without,hello,bag,world"

# Split the input string into a list
words = input_string.split(',')

# Sort the list alphabetically
words.sort()

# Join the sorted list into a string
sorted_string = ','.join(words)
print(sorted_string)
