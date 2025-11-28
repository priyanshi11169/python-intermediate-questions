# Write a function that counts how many times a letter appears in a string.

def count_letter(word):
  letter = input("Enter the letter to check: ")
  count = 0
  
  for char in word:
    if char in letter:
      count+=1
      
  print(f"count of letter {letter} is {count}")
      
count_letter("hellooo")
count_letter("how are you")
  
  
