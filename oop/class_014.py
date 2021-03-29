class Employee():

    num_of_emps = 0
    raise_amount = 1.04 # Class Variable

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + "." + last_name + "@company.com"

        Employee.num_of_emps += 1 # Employee.attribute - it can't be overwritten by the instances of the class

    def full_name(self): # A regular method automatically takes in the instance as the first argument
        return f"{self.first_name} {self.last_name}"
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first_name, last_name, pay, prog_lang):
        super().__init__(first_name, last_name, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    
    def __init__(self,  first_name, last_name, pay, employees=None):
        super().__init__(first_name, last_name, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_employees(self):
        for emp in self.employees:
            print("-->", emp.full_name())



if __name__ == '__main__':
    dev_1 = Developer("Joseph", "Jaraba", 50000, "Python")
    dev_2 = Developer("Corey", "Schafer", 60000, "Java")

    mgr_1 = Manager("Sue", "Smith", 9000, [dev_1])
    mgr_1.add_employee(dev_2)
    mgr_1.remove_employee(dev_1)
    mgr_1.print_employees()


    # print(help(Developer))
    # print(dev_1.email)
    # print(dev_1.prog_lang)

    print(isinstance(mgr_1,Employee))
    print(issubclass(Developer,Employee))

