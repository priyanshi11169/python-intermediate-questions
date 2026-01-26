'''Create a class Employee with the following:
🔹 Employee (Base Class)
Attributes:
name
salary
Method:
display() → prints name and salary
🔹 Manager (Derived Class – inherits Employee)
Additional attributes
bonus
Override the display() method to:
Call the parent display() method
Then print the bonus
Also print total salary = salary '''


class Employee():
  def __init__(self, name, salary):
    self.name = name
    self.salary = salary
  
  def display(self):
    print(f"The Salary of {self.name} is {self.salary}")

class Manager(Employee):
  
  def __init__(self, name, salary, bonus):
    super().__init__(name, salary)
    self.bonus = bonus
  
  def display(self):
     super().display()
     print(f"bonus is {self.bonus}")
     print(f"total salary is {self.salary + self.bonus}")
  
k = Manager("kaushik", 50000 ,10000)
k.display()
