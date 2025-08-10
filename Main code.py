import enum
from uuid import uuid4


class Gender(str, enum.Enum):
    """enum to store values of genders"""

    Male = "Male"
    Female = "Female"


class Person:
    def __init__(
        self,
        name: str = "John Doe",
        age: int = 0,
        ssn: str = "0000000000",
        gender: Gender = Gender.Male,
    ):
        self.name = name
        self.age = age
        self.ssn = ssn
        self.gender = gender

    def name_setter(self):
        self.name = input("\nEnter name: ").title()
        while True:
            if not (self.name.replace(" ", "").isalpha()):
                print("Wrong name entry valid name should be letters and spaces only.")
                self.name = input("\nEnter valid name: ")
            else:
                break

    def age_setter(self):
        self.age = int(input("Enter age: "))

    def SSN_setter(self):
        while True:
            self.ssn = input("Enter SSN: ")
            if len(self.ssn) != 10 or not self.ssn.isdigit():
                print("SSN must be a 10-digit number.")
            else:
                break

    def import_data_from_user(self):
        self.name_setter()
        self.age_setter()
        self.SSN_setter()

    def display_info(self):
        print(f"\nName: {self.name}, Age: {self.age}, SSN: {self.ssn}.")


class Majors(str, enum.Enum):
    """enum to store values of majors"""

    Artificial_Intelligence_And_Data_Science = "AI_DS"
    Computer_Science = "CS"
    Software_Engineering = "SE"
    Computer_Engineering = "CE"


class YearOfCollege(enum.Enum):
    """enum to store values of year of college"""

    Freshman = "Freshman"
    Sophomore = "Sophomore"
    Junior = "Junior"
    Senior = "Senior"


class Student(Person):
    def __init__(
        self,
        name: str = "",
        age: int = 0,
        ssn: str = "",
        gender: Gender = Gender.Male,
        major: Majors = Majors.Artificial_Intelligence_And_Data_Science,
        year_of_college: YearOfCollege = YearOfCollege.Freshman,
    ):
        super().__init__(name, age, ssn, gender)
        self.student_id = str(uuid4())[-8:-1]
        self.major = major
        self.year_of_college = year_of_college

    def major_setter(self):
        while True:
            temp = input("Enter major (AI_DS, CS, SE, CE): ").upper()
            if temp in Majors:
                self.major = Majors(temp)
                break
            else:
                print("Invalid major. Please enter a valid major (AI_DS, CS, SE, CE).")

    def year_of_college_setter(self):
        while True:
            temp = input(
                "Enter year of college (Freshman, Sophomore, Junior, Senior): "
            ).title()
            if temp in YearOfCollege:
                self.year_of_college = YearOfCollege(temp)
                break
            else:
                print(
                    "Invalid year of college. Please enter a valid year (Freshman, Sophomore, Junior, Senior)."
                )

    def import_data_from_user(self):
        super().import_data_from_user()
        self.major_setter()
        self.year_of_college_setter()
        print(
            f"-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-\nStudent data created successfully.\nStudent ID is : {self.student_id}."
        )

    def display_info(self):
        super().display_info()
        print(
            f"Student ID: {self.student_id}, Major: {self.major}, Year of College: {self.year_of_college}.\n"
        )


class StudentsDB:
    def __init__(self):
        self.students: Student = []

    def creat_DB(self):
        number_of_students = int(
            input("How Many students you want for the data base? \n")
        )
        for i in range(0, number_of_students):
            student = Student()
            print(f"For student number {i+1} please ")
            student.import_data_from_user()
            self.students.append(student)

    def read_DB(self):
        for i in range(self.students.__len__()):
            self.students[i].display_info()

    def update_DB(self):
        if self.students.__len__() == 0:
            print("Error, cant update empty database.")

        else:
            studentID = input(
                "Please enter the student ID whose information you want to update.\n"
            )
            studentIDX = -1
            for i in range(len(self.students)):
                if self.students[i].student_id == studentID:
                    studentIDX = i
                    break
                else:
                    print(
                        f"Error, student with {studentID} not found in the database.\n"
                    )
                    return

            while True:
                choice = int(
                    input(
                        "Sellect number of information to update from the list below : \n1. Student Name.\n2. Student age.\n3. Student major.\n4. Student year of college.\n"
                    )
                )
                if choice == 1:
                    self.students[studentIDX].name_setter()
                    break
                elif choice == 2:
                    self.students[studentIDX].age_setter()
                    break
                elif choice == 3:
                    self.students[studentIDX].major_setter()
                    break
                elif choice == 4:
                    self.students[studentIDX].year_of_college_setter()
                    break
                else:
                    print("Error, wrong entry please retry.\n")


TTU_students = StudentsDB()
TTU_students.creat_DB()
TTU_students.read_DB()
TTU_students.update_DB()
TTU_students.read_DB()
