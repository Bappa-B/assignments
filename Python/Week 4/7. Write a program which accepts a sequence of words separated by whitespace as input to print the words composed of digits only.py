# Input string
input_string = "2 cats and 3 dogs."

# Split the input string into a list of words
words = input_string.split()

# Filter words that are composed of digits only
digit_words = [word for word in words if word.isdigit()]

print(digit_words)
