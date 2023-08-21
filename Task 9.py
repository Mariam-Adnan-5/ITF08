with open("ITF8.txt","a") as file:
 name=input("Enter your name")
 age=input("Enter your age")
 DOB=input("Enter your Date of Birth")
 file.write(name+"\t")
 file.write(age+"\t")
 file.write(DOB+"\n")
 file.close()







