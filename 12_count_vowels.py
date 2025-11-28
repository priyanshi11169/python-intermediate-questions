# Write a function to count how many vowels are in a string.

def count_vowels(word):
  
  vowels = "aeiou"
  
  count = 0
  
  for char in word:
    if char in vowels:
      count+=1
      
  print(f"the number pf vowels in word {word} is {count}")
    
count_vowels("priyanshi")  
count_vowels("rishika")  
count_vowels("nikki")  

