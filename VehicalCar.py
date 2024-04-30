class Vehical:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    def get_make(self):
        return  self.make

    def get_model(self):
        return self.model

    def set_year(self,new_year):
        self.year=new_year

    def get_year(self):
        return  self.year

class Car(Vehical):

    def __init__(self,num_doors,):
        self.num_doors=num_doors

    def get_num_doors(self):
        return self.num_doors

vehi = Vehical("Honda","Passion Pro",1985)
print("MAKE OF VEHICAL:--",vehi.get_make())
print("MODEL OF VEHICAL:--",vehi.get_model())
print("YEAAR OF VEHICAL:--",vehi.get_year())
print("-----------------------------------------------------------")
vehi.set_year(2005)
print("Year of new_Vehical:--",vehi.get_year())
print("-----------------------------------------------------------")
cr = Car(4)
print("NUMBER OF DOORS:--",cr.get_num_doors())