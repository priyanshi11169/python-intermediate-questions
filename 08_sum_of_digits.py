# write a function that print the sum of digits.

def sum_of_digits(n):
  
  sum = 0 
  
  for i in range(n+1):
    sum+=i
  print(sum)
  
sum_of_digits(15)
