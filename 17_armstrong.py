# Write a function that checks whether a number is Armstrong like 153.

def is_armstrong(n):
  
  original = n
  
  total = 0
  
  while ( n > 0 ):
    digit = n % 10
    total = total + (digit**3)
    n = n // 10
  
  if (total == original):
    print("yes")
    
  else:
    print("No")
    
is_armstrong(153)