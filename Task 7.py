list=[]
avarge=[]
grads=[]
minimum=[]
maximum=[]
students_numbers=int(input("Enter the number of students"))
for i in range(students_numbers):
    x=int(input(f"Enter the number of marks for student{i+1}"))
    list.append(x)
sum=0
for i in range(students_numbers):
    for j in range(list[i]):
        mark=int(input(f"Enter mark{j+1}for student {i+1}"))
        grads.append(mark)
        sum+=mark
    avarge.append(sum/list[i])
    maximum.append(max(grads))
    minimum.append(min(grads))
    grads.clear()
    sum=0
for i in range(students_numbers):
    print(f"Student{i+1}\n Avarge={avarge[i]}\n Min={minimum[i]}\nMax={maximum[i]}")






