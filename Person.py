class Person:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def Display(self):
        print(f"Name:--{self.name}")
        print(f"Age:--{self.age}")


class Student(Person):
    def __init__(self,name,age,section):
        super().__init__(name,age)
        self.section=section

    def StudentDisplay(self):
        print(f"Name:--{self.name}")
        print(f"Age:--{self.age}")
        print(f"Section:--{self.section}")

per = Person("Sakshi",25)
per.Display()
print("------------------------------------------------------")
stud=Student("Shamal","27",'B')
stud.StudentDisplay()