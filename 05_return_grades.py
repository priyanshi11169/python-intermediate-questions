# write a function that returns grade (A/ B/ C/ D/ F) based on marks.

def result(marks):
  if marks >= 90 and marks <=100:
    return "A Grade"
  if marks >= 80 and marks < 90:
    return "B Grade"
  if marks >= 70 and marks < 80:
    return "c Grade"
  if marks >= 60 and marks < 70:
    return "D Grade"
  else:
    return "F Grade"
  
print(result(45))
print(result(90))