#Write a function that checks whether a string contains at least one uppercase, one lowercase, and one digit.

def string_contains(word):
  for char in word:
    if ( char.upper() in word) or ( char.lower() in word) or ( char == int(char)):
      return "yes"
    else:
      return "no"
    
print(string_contains("jiya"))
      