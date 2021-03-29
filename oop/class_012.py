class Employee():

    num_of_emps = 0
    raise_amount = 1.04 # Class Variable

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + "." + last_name + "@company.com"

        Employee.num_of_emps += 1 # Employee.attribute - it can't be overwritten by the instances of the class

    def full_name(self):
        return f"{self.first_name}, {self.last_name}"
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


print(Employee.num_of_emps)

emp_1 = Employee("Joseph", "Jaraba", 50000)
emp_2 = Employee("Corey", "Schafer", 60000)

print(Employee.num_of_emps)

emp_1.raise_amount = 1.05

print(emp_1.__dict__)

print(Employee.raise_amount)
print(emp_1.raise_amount) # The instance don't have the raise_amount itself, it's accessing the class's attribute
print(emp_2.raise_amount)
