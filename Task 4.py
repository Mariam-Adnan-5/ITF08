def Tringle():
  b=float(input("Enter base"))
  h=float(input("Enter Highe"))
  x=float(input("Enter third side"))
  area = b * h / 2
  per = b + h + x
  print(f"The Area is{area} \nThe perimeter is{per} ")

def square():
 b= float(input("Enter base"))
 area=b*b
 per=4*b
 print(f"The Area is{area} \nThe perimeter is{per} ")

print("To calculate the area & perimeter of triangle")
Tringle()
print("To calculate the area & perimeter of square")
square()