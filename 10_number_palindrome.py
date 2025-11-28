# Write a function that checks if a number is a palindrome (reverse == original).

def is_palindrome(n):
  
  original = n 
  n = abs(n)
  
  reverse = 0
  
  while ( n > 0):
    digit = n % 10
    reverse = reverse*10 + digit
    n = n // 10
    
  if ( reverse == abs(original)):
    print("Palindrome")
  
  else:
    print("Not a Palindrome")    
    
is_palindrome(121)
is_palindrome(123)
    
