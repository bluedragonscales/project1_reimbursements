# Set up any objects here before E2E tests run and tear them back down when the E2E tests are done.

from behave.runner import Context
from selenium import webdriver
from E2E_tests.page_object_models.employee_page import EmployeePage


def before_all(context):
    context.driver = webdriver.Chrome("E2E_tests/chromedriver.exe")
    context.employee_page = EmployeePage(context.driver)


def after_all(context):
    context.driver.quit()
