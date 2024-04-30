class Employee:

    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def set_salary(self,new_salary):
        self.salary=new_salary

    def get_salary(self):
        return self.salary


    def calulate_bonus(self,bonus_percentage):
        bonus=(self.salary*bonus_percentage)/100
        return bonus



class Manager(Employee):

    def __init__(self,department,name,id,salary):
        super().__init__(name,id,salary)
        self.department=department

    def get_department(self):
        return self.department



emp = Employee("Ranjit",1234,50000)
name1=emp.get_name()
id1=emp.get_id()
salary1=emp.get_salary()
print(f"Name of employee is {name1}")
print(f"Id of employee is {id1}")
print(f"Salary of employee is {salary1}")
print("----------------------------------------------")
emp.set_salary(60000)
bonus1=emp.calulate_bonus(20)
print(f"Salary of Employee is {emp.get_salary()}")
print(f"Bonus of Employeee is {bonus1}")
print("----------------------------------------------")
mana= Manager("Devloper","Shayam",6286,40000)
name2=mana.get_name()
id2=mana.get_id()
salary2=mana.get_salary()
department1=mana.get_department()

print(f"Name of Manager is {name2}")
print(f"Id of Manager is {id2}")
print(f"Salary of Manager is {salary2}")
print(f"Department of Manager is {department1}")

print("--------------------------------------------")

bonus2=mana.calulate_bonus(30)
print(f"Bonus of Manager if {bonus2}")
