#Write a function that returns "Even" if a number is even, "Odd" otherwise.

def is_even_odd(num):
  
  if ( num % 2 == 0):
    return "Even"
  else:
    return "Odd"
  
n = int(input("Enter a number: "))
print(is_even_odd(n))