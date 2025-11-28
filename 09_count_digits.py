# write a function that count the number of digits.

def count_digits(n):
  
  count = 0
  
  while ( n > 0 ):
    n = n // 10
    count+=1
  
  print(count)
  
count_digits(2469742)
    