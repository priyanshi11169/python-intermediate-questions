# Write a function that takes a sentence and returns the longest word.

sentence = "Python is an amazing programming language"

# split sentence into words
words = sentence.split()

# variable to store longest word
longest = ""

for i in words:
  if len(i) > len(longest):
    longest = i
print(longest)
