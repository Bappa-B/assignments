# 1. Reverse a string
input_string = "hello"
reversed_string = input_string[::-1]
print(f"Reversed string: {reversed_string}")

# 2. Check if the string is a palindrome
is_palindrome = input_string == reversed_string
print(f"Is palindrome: {is_palindrome}")

# 3. Check if it ends with a specific substring
substring = "lo"
ends_with = input_string.endswith(substring)
print(f"Ends with '{substring}': {ends_with}")

# 4. Capitalize the first letter of each word
capitalized_string = input_string.title()
print(f"Capitalized string: {capitalized_string}")

# 5. Check if two strings are anagrams
string1 = "listen"
string2 = "silent"
is_anagram = sorted(string1) == sorted(string2)
print(f"Are anagrams: {is_anagram}")

# 6. Remove vowels from the string
vowels = "aeiouAEIOU"
no_vowels_string = ''.join([char for char in input_string if char not in vowels])
print(f"String without vowels: {no_vowels_string}")

# 7. Find the length of the longest word in a sentence
sentence = "Practice makes perfect"
words = sentence.split()
longest_word = max(words, key=len)
print(f"Length of the longest word '{longest_word}': {len(longest_word)}")
