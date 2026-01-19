# Write a Python program to check whether two given strings are anagrams of each other

s1 = "silent"
s2 = "listen"

if sorted(s1) == sorted(s2):
  print("true")
else:
  print("false")