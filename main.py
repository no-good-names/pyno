import math

class Cal:
  def __init__(self):
    self.num = int(input("Enter a number: "))
    self.num1 = int(input("Enter a second number: "))
    self.add = self.num + self.num1
    
  def eq(self):
    print(self.add)
    
  def run(self):
    self.eq
 
if __name__ == "__main__":
  cal = Cal
  cal.run
