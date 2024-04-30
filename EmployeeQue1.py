class Employee:

    def __init__(self,id,name,salary):
        self.id = id
        self.name=name
        self.salary=salary

    def get_id(self):
        return self.id


    def get_name(self):
        return  self.name

    def set_salary(self,new_salary):
        self.salary=new_salary

    def get_salary(self):
        return self.salary

    def create_bonus(self,bonuscount):
        bonus_amount=(self.salary*bonuscount)/100
        return bonus_amount


emp=Employee(101,"Rihana",50000)
print("Employee_ID:-",emp.get_id())
print("Employee_NAME:-",emp.get_name())
print("Employee_SALARY:-",emp.get_salary())

emp.set_salary(60000)
print("Employee_NEW_SALARY:-",emp.get_salary())


bonuscount=emp.create_bonus(20)
print("Employee_BonusAmount:-",bonuscount)


