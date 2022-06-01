# Functions
# def func(x, y, z = None):
#     print('Run', x,y, z)
#     return x*y, x/y
#
# r1, r2 = func(5,6, 7)
# print (r1, r2)

# def func(x):
#     def func2():
#         print(x)
#     return func2
#
# x= func(3)
# x()

# #arguments and keyword arguments
# def func(*args, **kwargs):
#     print(args, kwargs)
#
# func(1,2,3,4,5, one = 0, two =1)
# #** -- used for dictionaries
# #* - used for lists

# # Finding largest/smallest number in a list
# x = [10, 5, 43, 31, 26]
# min = x[0]
# for i in x:
#     if i < min:
#         min = i
# print(min)

# # Reading and Writing Files
# with open('test.txt', 'r') as rf:
#     with open('test2.txt', 'w') as wf:
#         for line in rf:
#             wf.write(line)

# Classes -- Part 1
# class Employee:
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@company.com'
#
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
#
#
# emp1 = Employee('Corey', 'Schafer', 60000)
# emp2 = Employee('Test', 'User', 50000)
#
# emp1.fullname()
# print(Employee.fullname(emp1))
# # print(emp2.fullname())

# Classes -- Part 2
# class Employee:
#
#     num_of_emps = 0
#     raise_amount = 1.04
#
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@company.com'
#
#         Employee.num_of_emps += 1
#
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
#
#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)
# #     Change occurs here
#
#
# print(Employee.num_of_emps)
#
# emp1 = Employee('Corey', 'Schafer', 60000)
# emp2 = Employee('Test', 'User', 50000)
#
#
#
# emp1.raise_amount = 1.05
#
# print(Employee.num_of_emps)

# Classes -- Part 3
# class Employee:
#
#     num_of_emps = 0
#     raise_amount = 1.04
#
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@company.com'
#
#         Employee.num_of_emps += 1
#
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
#
#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)
#
#     @classmethod
#     def set_raise_amount(cls, amount):
#         cls.raise_amount = amount
# #     Change occurs here
#
# emp1 = Employee('Corey', 'Schafer', 60000)
# emp2 = Employee('Test', 'User', 50000)
#
# emp_str_1 = 'John-Doe-70000'
# emp_str_2 = 'Steve-Smith-30000'
# emp_str_3 = 'Jane-Doe-90000'
#
# first, last, pay = emp_str_1.split('-')
# new_emp1 = Employee(first, last, pay)
#
# print(new_emp1.email)
# print(new_emp1.pay)

# temperature = int(input("What is the temperature today? "))
# if temperature > 30:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif temperature > 20:
#     print("It's a nice day")
# elif temperature > 10:
#     print("It's a bit cold")
# else:
#     print("It's cold")
# print("Done")
