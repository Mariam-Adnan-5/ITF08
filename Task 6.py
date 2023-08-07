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
def circle():
  while True:
   radice=float(input("Enter the raduice"))
   if radice<0:
       print("Enter a positive radice")
       continue
   area=3.14*radice*radice

   print(f"The Area is{area}  ")
   break
def rectangle():
  while True:
   b= float(input("Enter base"))
   h = float(input("Enter Highe"))
   if b<0 or h<0 :
       print("Enter a positive sides")
       continue
   area=b*h

   print(f"The Area is{area}  ")
   break

def Tringle():
  while True:
    b=float(input("Enter base"))
    h=float(input("Enter Highe"))

    if b<0 or h<0 :
        print("Enter a positive sides")
        continue
    area = b * h / 2

    print(f"The Area is{area} ")
    break
while True:
    print(""""    1-To calculate the area of triangle
     2-To calculate the area  of rectangle
     3-To calculate the area  of circle
     4-Sum
     5-Subtract
     6-Muliply
     7-Division
     8-Exsit""")
    while True:
        choice = int(input("Enter your choice from{1 ,4}"))
        if choice == 1:
            Tringle()
            break

        elif choice ==2:
            rectangle()
            break

        elif choice == 3:
            circle()
            break

        elif choice == 4:
            num1 = int(input("Enter number 1"))
            num2 = int(input("Enter number2"))
            print(add(num1, num2))
            break
        elif choice == 5:
            num1 = int(input("Enter number 1"))
            num2 = int(input("Enter number2"))
            print(sub(num1, num2))
            break
        elif choice == 6:
            num1 = int(input("Enter number 1"))
            num2 = int(input("Enter number2"))
            print(mult(num1, num2))
            break
        elif choice == 7:
            num1 = int(input("Enter number 1"))
            num2 = int(input("Enter number2"))
            print(div(num1, num2))
            break
        elif choice == 8:
            print("Bye Bye")
            exit()
        else :
            print("invalid input")
            continue