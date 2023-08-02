def add(num1,num2):
   add=num1+num2
   return add

def sub(num1, num2):
   sub = num1 - num2
   return sub

def mult(num1,num2):
   mult=num1*num2
   return mult

def div(num1,num2):
   div=num1/num2
   return div


num1=input("Enter number 1")
num2=input("Enter number2")

print("The sub of 2 number")
print(sub(num1,num2))

print("The mult of 2 number")
print(mult(num1,num2))

print("The division of 2 number")
print(div(num1,num2))
