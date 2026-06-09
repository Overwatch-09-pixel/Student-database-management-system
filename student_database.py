print("===STUDENT DATABASE===")
name = input("Name: ")
print(f"Welcome {name}\nSelect one of the options below")
students = []
next_id = 0

while True:
  print("1. Add Student")
  print("2. View Students")
  print("3. Search Student")
  print("4. Update Student")
  print("5. Remove Student")
  print("6. Save Students")
  print("7. Load Students")
  print("8. Exit")

  choice = input("Enter your choice: ")

  if choice == "1":
    next_id += 1
    student_name = input("Name: ")
    student_department = input("Enter your department: ")
    current_year = int(input("Year: "))
    student_year = int(input("Student year: "))

    student = {
      "ID": next_id,
      "Name": student_name,
      "Department": student_department,
      "Year": current_year,
      "Student_year": student_year
    }
    students.append(student)
    print("Student added successfully!")
    print(f'Student ID: {next_id}')

  elif choice == "2":
    if len(students) == 0:
      print("No record")
    else:
      for student in students:
        print("Student ID: " , student['ID'])
        print("Name: " , student['Name'])
        print("Department: " , student['Department'])
        print("Year" , student['Year'])
        print("Student Year" , student["Student_year"])

  elif choice == "3":
    search = int(input("Enter ID to search: "))
    found = False
    for student in students:
      if student["ID"] == search:
        found = True
        print("Student found")
        print("ID: " , student["ID"])
        print("Name: " , student['Name'])
        print("Department: " , student["Department"])
        print("Year: " , student["Year"])
        print("Student Year: " , student["Student_year"])
        break
    if not found:
        print("Student not found")

  elif choice == "4":
    update = int(input("Enter student ID: "))
    found = False
    for student in students:
      if student['ID'] == update:
        found = True
        new_department = input("New department: ")
        new_year = input("Year update: ")
        new_student_year = input("Student year update: ")
        student["Department"] = new_department
        student["Year"] = new_year
        student["Student_year"] = new_student_year
        print("Student information updated successfully!")
        break
    if not found:
      print("No information found")

  elif choice == "5":
    remove = int(input("Student ID: "))
    found = False
    for student in students:
      if student["ID"] == remove:
        found = True
        students.remove(student)
        print("Student removed successfully!")
        break

    if not found:
      print("Error!\nStudent not found")

  elif choice == '6':
    file = open("students.txt" , "w")
    for student in students:
      file.write(str(student["ID"]) + "," + student["Name"] + "," + student["Department"] + "," + str(student["Year"]) + "," + str(student["Student_year"]) + "\n")
    print("Student data saved succesfully")
    file.close()

  elif choice == "7":
    students.clear()
    file = open("students.txt" , "r")
    for line in file:
      data = line.strip().split(",")
      student ={
        "ID": int(data[0]),
        "Name": data[1],
        "Department": data[2],
        "Year": int(data[3]),
        "Student_year": int(data[4])
      }
      students.append(student)
    print("Load successful")
    print("Students loaded: " , len(students))
    file.close()

  elif choice == "8":
    print("See you next time\nGood bye")
    break
