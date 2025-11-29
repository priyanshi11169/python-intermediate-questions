def odd_even_tuple():
  integers = ( 23, 56, 33, 68, 35, 43, 2, 5, 8)
  even_num= []
  odd_num= []
  

  for  num in integers:
    if ( num % 2 == 0):
      even_num.append(num)
    else:
      odd_num.append(num)
      
  print(f" A tuple of all even numbers are {tuple(even_num)}")
  
  print(f" A tuple of all even numbers are {tuple(odd_num)}")
  
  
odd_even_tuple()
      
      
      
      