def load_data():
 dict_list = []
 with open("Finall project.txt", "r") as file:
      lines = file.readlines()

      for line in lines:
            line = line.replace("\n"," ")
            line=line.split("|")
            student={
                "number":line[0],
                "id":line[1],
                "name": line[2],
                "age": line[3]
            }
            dict_list.append(student)
      print("Data loaded Successfully")
      return dict_list







