# Set up any objects here before E2E tests run and tear them back down when the E2E tests are done.

from behave.runner import Context
from selenium import webdriver
from E2E_tests.page_object_models.employee_page import LoginPage


def before_all(context):
    context.driver = webdriver.Chrome("chromedriver.exe")
    context.employee_page = LoginPage(context.driver)


def after_all(context):
    context.driver.quit()
