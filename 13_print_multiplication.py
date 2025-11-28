# Write a function that takes a number n and prints a multiplication table (1 to 10).

def multiplication_table(n):
  
  for i in range(1,10+1):
    print(f"{n} X {i} = {n*i}")
    
multiplication_table(5)
multiplication_table(2)