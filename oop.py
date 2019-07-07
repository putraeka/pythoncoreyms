# Tutorial dari https://youtu.be/ZDa-Z5JzLYM

class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@somecompany.com'
        
    def fullname(self):
        return f'{self.first} {self.last}'
        

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('User', 'Test', 60000)

print(emp_1.email.lower())
print(emp_2.email.lower())
print(emp_1.fullname())


# print(emp_1)
# print(emp_2)

# emp_1.first = 'Corey'
# emp_1.last = 'Schafer'
# emp_1.email = 'corey.schafer@somecompany.com'
# emp_1.pay = 50000

# emp_2.first = 'Test'
# emp_2.last = 'User'
# emp_2.email = 'test.user@somecompany.com'
# emp_2.pay = 60000