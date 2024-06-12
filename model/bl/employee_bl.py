from controller import *
from model.da.da import DataAccess
from model.entity import Employee

employee_da = DataAccess(Employee)


class EmployeeBl:
    @staticmethod
    def save(employee):
        return employee_da.save(employee)

    @staticmethod
    def edit(employee):
        if employee_da.find_by_employee_id(employee.employee_id):
            return employee_da.edit(employee)
        else:
            raise EmployeeNotFoundError()

    @staticmethod
    def remove(employee_id):
        employee = employee_da.find_by_employee_id(employee_id)
        if employee:
            return employee_da.remove(employee)
        else:
            raise EmployeeNotFoundError()

    @staticmethod
    def find_all():
        employee_list = employee_da.find_all()
        if employee_list:
            return employee_list
        else:
            raise EmployeeNotFoundError()

    @staticmethod
    def find_by_id(employee_id):
        employee = employee_da.find_by_employee_id(employee_id)
        if employee:
            return employee
        else:
            raise EmployeeNotFoundError()

    @staticmethod
    def find_by_family(family):
        employee_list = employee_da.find_by(Employee.family == family)
        if employee_list:
            return employee_list
        else:
            raise EmployeeNotFoundError()

    @staticmethod
    def find_by_username(user_name):
        employee_list = employee_da.find_by(Employee.user_name == user_name)
        if employee_list:
            return employee_list
        else:
            raise UsernameNotFoundError()

    @staticmethod
    def find_by_password(password):
        employee_list = employee_da.find_by(Employee.password == password)
        if employee_list:
            return employee_list
        else:
            raise PasswordNotFoundError()
