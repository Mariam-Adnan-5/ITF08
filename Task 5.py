def test(area):
 if area>=10:
     print("The Area is huge")
 elif   0<area<10:
     print("The Area is small")
 else :
     print("invalid input")

def Tringle():
  b=float(input("Enter base"))
  h=float(input("Enter Highe"))
  x=float(input("Enter third side"))
  area = b * h / 2
  per = b + h + x
  print(f"The Area is{area} \nThe perimeter is{per} ")
  test(area)

def rectangle():
 b= float(input("Enter base"))
 h = float(input("Enter Highe"))
 area=b*h
 per=(2*b)+(2*h)
 print(f"The Area is{area} \nThe perimeter is{per} ")
 test(area)
def circle():
  radice=float(input("Enter the raduice"))
  area=3.14*radice*radice
  per=2*3.14*radice
  print(f"The Area is{area} \nThe perimeter is{per} ")
  test(area)

print("To calculate the area & perimeter of triangle")
Tringle()
print("To calculate the area & perimeter of rectangle")
rectangle()
print("To calculate the area & perimeter of circle")
circle()
