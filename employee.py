"""Employee pay calculator."""

class Employee:
    def __init__(self, name, contract_number = 0, contract_rate = 0, bonus = 0):
        self.name = name
        self.contract_number = contract_number
        self.contract_rate = contract_rate
        self.bonus = bonus

    def set_contracts(self, contract_number, contract_rate):
        self.contract_number = contract_number
        self.contract_rate = contract_rate

    def set_bonus(self, bonus):
        self.bonus = bonus

    def add_commission(self):
        commission = 0
        if self.contract_number and self.contract_rate:
            commission += self.contract_number * self.contract_rate
        elif self.bonus:
            commission += self.bonus
        else:
            return 0
        return commission

    def get_pay(self):
        pass

    def __str__(self):
        pass

class Salary_Employee(Employee):
    def __init__(self, name, salary, contract_number = 0, contract_rate = 0, bonus = 0):
        super().__init__(name, contract_number, contract_rate, bonus)
        self.salary = salary

    def get_pay(self):
        return self.salary + self.add_commission()

    def __str__(self):
        description = f"{self.name} works on a monthly salary of {self.salary}"
        if self.contract_number and self.contract_rate:
            description += f" and receives a commission for {self.contract_number} contract(s) at {self.contract_rate}/contract."
        elif self.bonus:
            description += f" and receives a bonus commission of {self.bonus}."
        else:
            description += "."
        description += f" Their total pay is {self.get_pay()}."
        return description

class Hourly_Employee(Employee):
    def __init__(self, name, hourly_rate, hours, contract_number = 0, contract_rate = 0, bonus = 0):
        super().__init__(name, contract_number, contract_rate, bonus)
        self.hourly_rate = hourly_rate
        self.hours = hours

    def get_pay(self):
        return (self.hourly_rate * self.hours) + self.add_commission()

    def __str__(self):
        description = f"{self.name} works on a contract of {self.hours} hours at {self.hourly_rate}/hour"
        if self.contract_number and self.contract_rate:
            description += f" and receives a commission for {self.contract_number} contract(s) at {self.contract_rate}/contract."
        elif self.bonus:
            description += f" and receives a bonus commission of {self.bonus}."
        else:
            description += "."
        description += f" Their total pay is {self.get_pay()}."
        return description


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Salary_Employee(name = 'Billie', salary = 4000)
billie.__str__()

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Hourly_Employee(name = 'Charlie', hourly_rate = 25, hours = 100)
charlie.__str__()

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Salary_Employee(name = 'Renee', salary = 3000)
renee.set_contracts(4, 200)
renee.__str__()

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Hourly_Employee(name = 'Jan', hourly_rate = 25, hours = 150)
jan.set_contracts(3, 220)
jan.__str__()

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Salary_Employee(name = 'Robbie', salary = 2000)
robbie.set_bonus(1500)
robbie.__str__()

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Hourly_Employee(name = 'Ariel', hourly_rate = 30, hours = 120)
ariel.set_bonus(600)
ariel.__str__()
