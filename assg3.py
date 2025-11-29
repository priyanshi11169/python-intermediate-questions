# input two list from user and merge and then sort.

def sort_list():
  list1 = list(map(int,input("enter numbers: ").split()))


  list2 = list(map(int,input("enter numbers: ").split()))

  list3 = list1 + list2

  list3.sort()

  print(list3)
  
sort_list()

