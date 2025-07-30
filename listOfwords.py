#Create a program that stores a list of words. Then, use list comprehension to create a new list that contains only the words that have an odd number of characters.

words = []
num_words = int(input("Enter the number of words you want to add: "))
for _ in range(num_words):
    word = input("Enter a word: ")
    words.append(word)

# Use list comprehension to filter words with odd length
odd_length_words = [word for word in words if len(word) % 2 == 1]

print("Words with an odd number of characters:", odd_length_words)