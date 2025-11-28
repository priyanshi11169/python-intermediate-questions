# Write a function that checks if a string is a palindrome (reverse == original).

def is_palindrome(word):
  
  reverse = ""
  
  for char in reversed(word):
    reverse+=char
    
  if (reverse == word):
    print("Palindrome")
    
  else:
    print("Not a Palindrome")
  
is_palindrome("madam")
is_palindrome("people")
  