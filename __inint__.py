# class definition
class Student:
    def __init__(self, fname, lname, age, section):
        self.firstname = fname
        self.lastname = lname
        self.age = age
        self.section = section
    
    def display_info(self):
        return f"First Name: {self.firstname}, Last Name: {self.lastname}, Age: {self.age}, Section: {self.section}"

# creating a new object
stu1 = Student("Dhoni", "Virat", 42, "A1")

# Display the student information
print(stu1.display_info())
