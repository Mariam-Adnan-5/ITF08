def load_data(data=[]):
 dict_list = []
 with open("Finall project.txt", "r") as file:
      lines = file.readlines()

      for line in data:
            line = line.get_student_details()
            dict_list.append(line)
      print("Data loaded Successfully")

      return dict_list

def update_data(data=[]):
    with open("Finall project.txt","a")as file:
        for items in data:
            file.writelines(str(items)+"\n")
        file.close()





