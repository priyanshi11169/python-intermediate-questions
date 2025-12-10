# Write a function that prints the Fibonacci series up to n terms.

def fibonacci(n):
  
  if ( n == 0):
    print("enter valid number")
    return
    
  a = 0
  b = 1
  
  # loop n times chalega ...if n = 5 so 0,1,2,3,4
  for i in range(n):
    print(a, end=" ")
    c = a+b 
    a = b
    b = c
    
fibonacci(8)