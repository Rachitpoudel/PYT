student_dict = {
    "Rachit": 21,
    "Apil": 19,
    "Rabi": 20,
    "Aadrasha": 22
}
student_name = input("Enter the name of the student: ")
if student_name in student_dict:
    print(f"{student_name}'s age is {student_dict[student_name]}.")
else:
    print(f"{student_name} is not in the dictionary.")
