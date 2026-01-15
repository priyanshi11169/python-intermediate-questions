# Given a list, create a dictionary of element frequencies.

# list
listi = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4]

# dict variable
frequency = {}

for i in listi:
  if i in frequency:
    frequency[i]+=1
  else: 
    frequency[i] = 1
  
print(frequency)