# Remove Duplicate Characters

input_word = input("Enter a word")

output = ""

for i in input_word:
  if i not in output:
    output +=i
  
print(output)