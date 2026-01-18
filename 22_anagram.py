# Group Anagrams

words = ["eat", "tea", "tan", "ate", "bat", "nat"]

anagram_dict = {}

for word in words:
  key = "".join(sorted(word))
  
  if key in anagram_dict:
    anagram_dict[key].append(word)
  
  else:
    anagram_dict[key] = [word]
    
print(anagram_dict)

# output --> {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']}
  