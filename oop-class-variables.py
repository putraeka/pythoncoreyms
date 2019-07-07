# Tutorial dari https://youtu.be/BJ-VvGyQxho

class Employee:
    
    num_of_emps = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@somecompany.com'
        
        Employee.num_of_emps += 1
        
    def fullname(self):
        return f'{self.first} {self.last}'
    
    def apply_raise(self):
        # Bisa menggunakan nama class (tapi ketika change semua akan terkena effect)
        # self.pay = int(self.pay * Employee.raise_amount) 
        # Bisa menggunakan self (jika menggunakan self hanya yang variable yang menggunakan
        # akan terkena effectnya)
        self.pay = int(self.pay * self.raise_amount)

print(Employee.num_of_emps)
        
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('User', 'Test', 60000)

print(Employee.num_of_emps)

# print(emp_1.__dict__)
# print(emp_1.email.lower())
# print(emp_2.email.lower())
# print(emp_1.fullname())
# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)