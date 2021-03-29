#Python OOP
import datetime

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
        return f"{self.first_name}, {self.last_name}"
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    #-Class Methods-#
    @classmethod # We work with the class instead of the instance
    def set_raise_amt(cls, amount): # cls - class varible name
        cls.raise_amount = amount

    @classmethod # Alternavite constructor 
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    #-Static Methods-#
    @staticmethod # Behave like regular functions, but they have some logical connection with the class
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee("Joseph", "Jaraba", 50000)
emp_2 = Employee("Corey", "Schafer", 60000)

# Employee.set_raise_amt(1.05)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# emp_str_1 = "John-Doe-70000"
# emp_str_2 = "Steve-Smith-30000"
# emp_str_3 = "Jane-Doe-90000"

# new_emp_1 = Employee.from_string(emp_str_1)

# print(new_emp_1.email)
# print(new_emp_1.pay)

my_date = datetime.date.today()
print(Employee.is_workday(my_date))


