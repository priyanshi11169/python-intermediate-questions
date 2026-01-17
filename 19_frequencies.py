# Given a list, create a dictionary of element frequencies.

# list
listi = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4]

frequency_dict = {}

for i in listi:
  
  if i in frequency_dict:
    frequency_dict[i] +=1
  else:
    frequency_dict[i] = 1

print(frequency_dict)