"""
Task 7_2
Create classes Employee, SalesPerson, Manager and Company with predefined functionality.

Create basic class Employee and declare following content:
• Attributes – `name` (str), `salary` and `bonus` (int), set with property decorator
• Constructor - parameters `name` and `salary`
• Method `bonus` - sets bonuses to salary, amount of which is delegated as `bonus`
• Method `to_pay` - returns the value of summarized salary and bonus.

Create class SalesPerson as class Employee inheritor and declare within it:
• Constructor with parameters: `name`, `salary`, `percent` – percent of plan performance (int, without the % symbol), first two of which are passed from basic class constructor
• Redefine method of parent class `bonus` in the following way: if the sales person completed the plan more than 100%, their bonus is doubled (is multiplied by 2), and if more than 200% - bonus is tripled (is multiplied by 3)

Create class Manager as Employee class inheritor, and declare within it:
• Constructor with parameters: `name`, `salary` and `client_number` (int, number of served clients), first two of which are passed to basic class constructor.
• Redefine method of parent class `bonus` in the following way: if the manager served over 100 clients, their bonus is increased by 500, and if more than 150 clients – by 1000.

Create class Company and declare within it:
• Constructor with parameters: `employees` – list of company`s employees (made up of Employee/SalesPerson/Manager classes instances) with arbitrary length `n`
• Method `give_everybody_bonus` with parameter company_bonus (int) that sets the amount of basic bonus for each employee.
• Method `total_to_pay` that returns total amount of salary of all employees including awarded bonus
• Method `name_max_salary` that returns name of the employee, who received maximum salary including bonus.

Note:
Class attributes and methods should bear exactly the same names as those given in task description
Methods should return only target values, without detailed explanation within `return`
"""
from typing import List


class Employee:
    def __init__(self, name: str, salary: int):
        self.__name = name
        self.__salary = salary
        self.__bonus = 0

    @property
    def name(self) -> str:
        return self.__name

    @property
    def salary(self) -> int:
        return self.__salary

    @property
    def bonus(self) -> int:
        return self.__bonus

    @bonus.setter
    def bonus(self, bonus: int) -> None:
        self.__bonus = bonus

    def to_pay(self) -> int:
        return self.__salary + self.bonus


class SalesPerson(Employee):
    def __init__(self, name, salary, percent):
        super(SalesPerson, self).__init__(name, salary)
        self.__percent = percent
        self.__bonus = 0

    @property
    def bonus(self) -> int:
        if self.__percent > 200:
            return 3 * self.__bonus
        elif self.__percent > 100:
            return 2 * self.__bonus
        else:
            return self.__bonus

    @bonus.setter
    def bonus(self, bonus: int) -> None:
        self.__bonus = bonus


class Manager(Employee):
    def __init__(self, name, salary, client_number):
        super(Manager, self).__init__(name, salary)
        self.__client_number = client_number
        self.__bonus = 0

    @property
    def bonus(self) -> int:
        if self.__client_number > 150 and self.__bonus:
            return self.__bonus + 1000
        elif self.__client_number > 100 and self.__bonus:
            return self.__bonus + 500
        else:
            return self.__bonus

    @bonus.setter
    def bonus(self, bonus: int) -> None:
        self.__bonus = bonus


class Company:
    def __init__(self, employees: List[Employee], n: int):
        self.__employees = employees

    def give_everybody_bonus(self, bonus: int) -> None:
        for employee in self.__employees:
            employee.bonus = bonus

    def total_to_pay(self) -> int:
        total = 0
        for employee in self.__employees:
            total += employee.to_pay()
        return total

    def name_max_salary(self) -> str:
        return max(self.employees, key=Employee.to_pay).name

    @property
    def employees(self):
        return self.__employees
