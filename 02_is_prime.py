# Write a function to check if a number is prime.

def is_prime(n):
  for i in range(2,n):
    if ( n % i == 0):
      print("Not a prime number")
      return 
  
  print("Prime number")
  
is_prime(5)
is_prime(4)