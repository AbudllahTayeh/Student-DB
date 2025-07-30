import enum
class Gender(str,enum.Enum):
    """enum to store values of genders"""
    Male="Male"
    Female="Female"
    
class Person:
    def __init__(self, name:str = "John Doe", age:int = 0, ssn:str = "0000000000", gender:Gender = Gender.Male):
        self.name = name
        self.age = age
        self.ssn = ssn
        self.gender = gender
    
    def import_data_from_user(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
        while(True):
            self.ssn = input("Enter SSN: ")
            if len(self.ssn) != 10 or not self.ssn.isdigit():
                print("SSN must be a 10-digit number.")
            else:
                break
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, SSN: {self.ssn}.\n")
class Majors(str, enum.Enum):
    """enum to store values of majors"""
    AI_DS = "AI & DS"
    CS = "Computer Science"
    SE = "Software Engineering"
    CE = "Computer Engineering"
class YearOfCollege(enum.Enum):
    """enum to store values of year of college"""
    Freshman = "Freshman"
    Sophomore = "Sophomore"
    Junior = "Junior"
    Senior = "Senior"
class Student(Person):
    def __init__(self, name : str = "", age : int = 0, ssn : str = "", gender : Gender = Gender.Male,
                  student_id : str = "", major :Majors = Majors.AI_DS, year_of_college :YearOfCollege = YearOfCollege.Freshman):
        super().__init__(name, age, ssn, gender)
        self.student_id = student_id
        self.major = major
        self.year_of_college = year_of_college
    def import_data_from_user(self):
        super().import_data_from_user()
        self.student_id = input("Enter student ID: ")
        self.major = Majors(input("Enter major (AI_DS, CS, SE, CE): "))
        self.year_of_college = YearOfCollege(input("Enter year of college (Freshman, Sophomore, Junior, Senior): "))
    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}, Major: {self.major}, Year of College: {self.year_of_college}.\n")
class StudentDB:
    def __init__(self):
        self.students = []
abdullah=Student()
abdullah.import_data_from_user()
abdullah.display_info()


