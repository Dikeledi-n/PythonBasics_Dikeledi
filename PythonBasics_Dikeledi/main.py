import mymodule

#use the greet function 
message = mymodule.greet("Dikeledi")
print(message)

#Create an object of the Calculator class
calc = mymodule.Calculator()

#Use the add and subtract method
result_add =calc.add(100, 150)
result_subtract =calc.subtract(100, 250)

print(f"Addition: {result_add}")
print(f"Subtraction: {result_subtract}")

#Person class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
        
#Student subclass
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        
    def display_student_id_info(self):
        self.display_info()
        print(f"Student ID: {self.student_id}")
        
#Create an object for Student
my_student = Student("Dikeled", 28, "DN12345")

#Call methods on the student
my_student.display_student_id_info()

#User input for name, age, student_id with error handling

try:
    name = input("Enter student's name: ")
    age = int(input("Enter student's age: "))
    student_id = input("Enter student's ID")
    
    if not student_id:
        raise ValueError("Student ID cannot be empty.")
    
#Create a student object and display its details
    student = Student(name, age, student_id)
    student.display_student_id_info()

except ValueError as e:
    print(f"Error: {e}. Please try again")


