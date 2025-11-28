# write a function that print the number of digits.

def print_digits(n):
  
  n = abs(n)
  
  digits = []
  
  while ( n > 0 ):
    digit = n % 10 
    digits.append(digit)
    n = n // 10  # after 3  n = 0 so while loop stops.
    
  for num in reversed(digits):
    print(num)
    
print_digits(312)
print_digits(-5402)
    