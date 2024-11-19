import pytest
from employee import Employee


def test_give_default_raise():
    employee = Employee('Betty', 'Johnson', 50000)

    initial_salary = employee.annual_salary

    employee.give_raise()

    assert employee.annual_salary == initial_salary + 5000



def test_give_custom_raise():
    employee = Employee('Betty', 'Johnson', 60000)

    initial_salary = employee.annual_salary

    employee.give_raise(10000)

    assert employee.annual_salary == initial_salary + 6000