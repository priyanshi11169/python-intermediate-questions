# “Create a dictionary from two lists”

keys = ["a", "b", "c"]
values = [1, 2, 3]

new_dict = {}

for i in range(len(keys)):
   new_dict[keys[i]] = values[i]
   
print(new_dict)