def large (list2=[]):
    list2.sort()
    largest=list2[len(list2)-1]
    return largest
def small(list2=[]):
    list2.sort()
    smallest=list2[0]
    return smallest
list=[]
count=int(input("How many number do you add"))
for i in range(count):
    number=int(input(f"Enter number{i+1}"))
    list.append(number)
print(f"The largest number is{large(list)}\nThe largest number is{small(list)}")