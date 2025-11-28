''' Write a function that returns True if a string is a valid password:
length ≥ 8
contains special character
contains uppercase,
contains lowercase,
contains a digit '''

def valid_pass(password):
  
  has_upper = False
  has_lower = False
  has_digit = False
  has_special = False
  
  special_char = "@#$%&"
  
  for char in password:
    if char.isupper():
      has_upper = True
    if char.islower():
      has_lower = True
    if char.isdigit():
      has_digit = True
    if char in special_char:
      has_special = True
      
  if (( len(password) >=8 ) and has_special and has_digit and has_upper and has_lower):
      print("Valid Password")
      
  else:
      print("Not a Valid Password")

valid_pass("jiya1@Aa")