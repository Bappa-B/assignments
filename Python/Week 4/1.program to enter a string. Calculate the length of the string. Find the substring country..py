# Input string
input_string = "India is my motherland. I love my country. Capital of India is New Delhi."

# Length of the string
length_of_string = len(input_string)
print(f"Length of the string: {length_of_string}")

# Finding the substring "country"
if "country" in input_string:
    print("Substring 'country' found.")
else:
    print("Substring 'country' not found.")

# Counting occurrences of each word
words = input_string.split()
word_count = {}
for word in words:
    word = word.strip('.,').lower()  # Removing punctuation and converting to lowercase
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word occurrences:")
for word, count in word_count.items():
    print(f"{word}: {count}")
