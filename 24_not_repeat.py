# Write a Python program to find the first character in a string that does not repeat

word = "aabbcddbe"
non_repeated_word  = ""

for i in word:
  
  if word.count(i) < 2:
    non_repeated_word+=i
    break
  
print(non_repeated_word)
    