# Import the context object we will use to utilize all of our steps.
from behave.runner import Context
# From the selenium package, import the built in web driver module
from selenium import webdriver
# From our POM package and the employee_portal module inside that package, import the class EmployeePage.
from page_object_models.employee_portal import EmployeePage



# This module must be named "environment" exactly because behave will be looking for it. This module will set up our
# end to end tests and then close them down when finished.


# This "before_all" method starts up the application tests. Inside it we need the web driver and the POM.
def before_all(context: Context):
    # The context object from the Behave framework calls the driver variable from the EmployeePage class. Then the
    # web driver module from selenium calls the Chrome class to create an instance with our web driver passed into its
    # constructor method. This creates our own web driver object which can be used for our steps.
    context.driver = webdriver.Chrome("chromedriver.exe")
    # We pass the new web driver object into the EmployeePage class's constructor to create an instance of that class.
    context.emp_home = EmployeePage(context.driver)
    # This tells the selenium automation to run in a maximized window instead of a minimized window.
    context.driver.maximize_window()



def after_all(context):
    context.driver.quit()