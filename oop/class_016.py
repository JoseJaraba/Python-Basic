class Employee():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property # makes able to access the email method like an attribute 
    def email(self): 
        return f"{self.first_name}.{self.last_name}@email.com"
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    @full_name.setter
    def full_name(self, name):
        first, last = name.split(" ")
        self.first_name = first
        self.last_name = last
    
    @full_name.deleter
    def full_name(self):
        print("Delete Name!")
        self.first_name = None
        self.last_name = None
    
if __name__ == '__main__': #Entry point
    emp_1 = Employee("John", "Smith")

    emp_1.full_name = "Jose Jaraba"

    print(emp_1.first_name)
    print(emp_1.email)
    print(emp_1.full_name)

    del emp_1.full_name