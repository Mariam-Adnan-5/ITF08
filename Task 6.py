def circle():
  while True:
   radice=float(input("Enter the raduice"))
   if radice<0:
       print("Enter a positive radice")
       continue
   area=3.14*radice*radice
   per=2*3.14*radice
   print(f"The Area is{area} \nThe perimeter is{per} ")
   break


def rectangle():
  while True:
   b= float(input("Enter base"))
   h = float(input("Enter Highe"))
   if b<0 or h<0 :
       print("Enter a positive sides")
       continue
   area=b*h
   per=(2*b)+(2*h)
   print(f"The Area is{area} \nThe perimeter is{per} ")
   break

def Tringle():
  while True:
    b=float(input("Enter base"))
    h=float(input("Enter Highe"))
    x=float(input("Enter third side"))
    if b<0 or h<0 or x<0:
        print("Enter a positive sides")
        continue
    area = b * h / 2
    per = b + h + x
    print(f"The Area is{area} \nThe perimeter is{per} ")
    break


while True:
    print(""""    1-To calculate the area & perimeter of triangle
     2-To calculate the area & perimeter of rectangle
     3-To calculate the area & perimeter of circle
     4-Exsit""")
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
            print("Bye Bye")
            exit()
        else :
            print("invalid input")
            continue