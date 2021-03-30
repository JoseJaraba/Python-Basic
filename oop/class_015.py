class Employee():

    num_of_emps = 0
    raise_amount = 1.04 # Class Variable

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + "." + last_name + "@company.com"

        Employee.num_of_emps += 1 # Employee.attribute - it can't be overwritten by the instances of the class
    
    def __repr__(self):
        return f"Employee({self.first_name}, {self.last_name}, {self.pay})"

    def __str__(self):
        return f"{self.full_name()} - {self.email}"

    def full_name(self): # A regular method automatically takes in the instance as the first argument
        return f"{self.first_name}, {self.last_name}"
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)