import random
from files_session import load_data, update_data
class Course:
    def __init__(self,course_name,course_mark):
        self.__course_name=course_name
        self.__course_mark=course_mark
        self.__course_id=random.randint(0,100)

    def set_course_name(self,course_name):
        self.__course_name=course_name
    def get_course_name(self):
       return self.__course_name
    def set_course_mark(self,course_mark):
        self.__course_name=course_mark
    def get_course_mark(self):
       return self.__course_mark
    def get_course_id(self):
        self.__course_id = random.randint(0, 100)
        return self.__course_id
    def course_append(self):
        with open("Finall project.txt", "a") as fileto:
         fileto.write(self.get_course_name() + "|" + str(self.get_course_mark()) + "|"+ str(self.get_course_id()) + "\n")

    def get_course(self):
        print(f"{self.__course_id}\t|{self.__course_name}\t|{self.__course_mark}")
class Student(Course):
    student_count=0
    def __init__(self,student_name,student_age,student_number):
       self.__student_name=student_name
       self.__student_age=student_age
       self.__student_number=student_number
       self.__student_id = random.randint(0, 100)
       self.course_list=[]

    def set_student_name(self,student_name):
        self.__student_name = student_name
    def get_student_name(self):
        return self.__student_name
    def set_student_age(self,  student_age):
        self.__student_age = student_age
    def get_student_age(self):
        return self.__student_age
    def set_student_number(self, student_number):
        self.__student_number = student_number
    def get_student_number(self):
        return self.__student_number
    def set_student_id(self,student_id):
        self.__student_id = student_id
    def get_student_id(self):
        return self.__student_id
    def get_student_details(self):
        students= {"student_number":self.__student_number,
                   "student_id":self.__student_id,
                   "student_name":self.__student_name,
                   "student_age":self.__student_age
                  # "course_list":self.
        }
        return students
    def dict_list(self):
        students = {"student_number": self.__student_number,
                    "student_id": self.__student_id,
                    "student_name": self.__student_name,
                    "student_age": self.__student_age}
        result_list=list(students.values())
        return result_list

    def new_course(self):
     with open("Finall project.txt", "r") as file:
        course_name = input("Enter course name")
        course_mark = int(input("Enter course mark"))
        course = Course(course_name, course_mark)
        self.course_list.append(course)
        course.course_append()

    def student_course(self):
        print("course_id\tcourse_name\tcourse_mark")
        for i in self.course_list:
          i.get_course()

    def mark_avarge(self,index):
        sum = 0
        count = 0
        for i in index.course_list:
                    sum += i.get_course_mark()
                    count += 1
        return sum / count
name=input("Enter your name")
submission_date=input("Enter submission_date")
print(f"name is :{name}\nsubmission_date is :{submission_date}")
students_list =load_data()
while True:
    selection=int(input(""" 1-Add New Student\n 2-Delete Student\n 3-Display Student\n 4-Get Student average
  5-Add course with student with mark\n 6-Exsit.\n Enter your choice """))
    if selection==1:
        student_name=input("Enter Student full name")
        while True:
         try:
          student_age=int(input("Enter Student age"))
          if student_age>0:
           break
          else:
              print("Invalid Input")
         except:
             print("Invalid Input")
        while True:
         try:
          student_number = int(input("Enter Student number"))
          if student_number>0:
           break
          else:
              print("Invalid Input(Enter positive student number)")
         except:
             print("Invalid Input")
        student=Student(student_name,student_age,student_number)
        students_list.append(student)
        update_data(students_list)


        print("Student Added Successfully -_-")
    elif selection==2:
        while True:
            try:
                student_number = int(input("Input Student number"))
                break
            except:
                print("Invalid input")
        for i in students_list:
          if student_number == i.get_student_number():
              students_list.remove(i)
              update_data(students_list)
              print("Student Deleted Successfully -_-")
              break
        else:
            print("Student Not exist")
    elif selection==3:
         while True:
            try:
                student_number = int(input("Input Student number"))
                break
            except:
                print("Invalid input")
         for i in students_list:
           if student_number == i.get_student_number():
             print(  i.get_student_details())
             i.student_course()
             break
         else:
            print("Student Not exist")

    elif selection==4:
        while True:
            try:
                student_number = int(input("Input Student number"))
                break
            except:
                print("Invalid input")
        for i in students_list:
            if student_number == i.get_student_number():
             print( i.mark_avarge(i))
        else:
            print("Student Not exist")

    elif selection==5:
        while True:
            try:
                student_number = int(input("Input Student number"))
                break
            except:
                print("Invalid input")
        for i in students_list:
            if student_number == i.get_student_number():
             i.new_course()
             print("Course Added Successfully -_-")
             break
        else:
            print("Student Not exist,please focus")
    elif selection==6:
        print("ByBy -_-")
        exit()
    else :
        print("Invalid Input")



