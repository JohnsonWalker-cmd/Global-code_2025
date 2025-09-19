sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()

# print(words)

#list comprehension

# [expression for item in iterable]

length_of_word = [len(word) for word in words]

#print(length_of_word)


without_the = [len(word) for word in words if word != 'the']


#print(without_the)


# Create a list containing only the even numbers from this list:

numbers = [12, 54, 33, 67, 24, 89, 11, 24, 47]

even_numbers = [ num for num in numbers if num % 2 == 0]
print(even_numbers)


#Create a list containing tuples of the uppercase version and the length of the following words:
words = ["hello", "my", "name", "is", "Sam"]
upper_and_length = [(word.upper(), len(word)) for word in words]

print(upper_and_length)