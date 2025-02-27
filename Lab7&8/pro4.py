"""Create a class "Employee" with attributes name and salary. Implement 
overloaded operators + and - to combine and compare employees based on
 their salaries."""

class Employee:
    def __init__(self, name, account_no, balance):
        self.name = name
        self.account_no = account_no
        self.balance = balance

    def add(self, other):
        sum_salary = self.balance + other.balance
        print("Sum of salaries of two employees is", sum_salary)

    def diff(self, other):
        difference = abs(self.balance - other.balance)
        print("Difference of salaries of two employees is", difference)


# Main
emp1 = Employee("abc", 1, 500)
emp2 = Employee("xyz", 2, 980)
emp1.add(emp2)
emp1.diff(emp2)
