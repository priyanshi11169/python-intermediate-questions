# Write a function that takes three numbers and returns the largest using only if-else (no max()).

def is_largest(a, b, c):
  if a > b and a > c:
    return f"{a} is the largest number"
  
  if b > a and b > c:
    return f"{b} is the largest number"
  
  else:
    return f"{c} is the largest number"
  
print(is_largest(2, 10, 7))
print(is_largest(55, 10, 17))