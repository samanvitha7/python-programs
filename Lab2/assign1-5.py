"""You are a student in a class of 10. Your class teacher assigns you a task of entering the names of all the students in the
 class. You finally want to display the names given the condition that the maximum allowed characters in a name is 15. As a fun 
 task, reverse the names and display them. [Hint: Slicing works when you are selecting maximum characters]"""

students = []
# taking input
for i in range(3):   #there are 10 students
    name = input("Enter name of student: ")
    students.append(name)

# Slicing and reversing
print("\nReversed Names (Maximum 15 characters):")
for name in students:
    sliced_name = name[:15]  # Perform slicing after input
    print(sliced_name[::-1])  # Reverse the sliced name

