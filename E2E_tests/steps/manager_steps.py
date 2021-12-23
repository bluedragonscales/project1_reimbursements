import time
from behave import Given, When, Then

# TO LOG IN
from selenium.webdriver.support.select import Select


@Given(u'the manager is on the login page.')
def get_manager_login_page(context):
    context.driver.get("file:///C:/Users/kckar/Desktop/Revature/project1_reimbursements/front-end/index.html")


@When(u'the manager inputs 2 into the manager id input box.')
def fill_manager_id(context):
    context.employee_page.select_manager_id_box().send_keys("2")


@When(u'the manager inputs acapella into the password box.')
def fill_manager_password(context):
    context.employee_page.select_manager_password_box().send_keys("acapella")


@When(u'the manager clicks the login button.')
def click_manager_login(context):
    context.employee_page.click_manager_login_button().click()


@Then(u'the manager is redirected to the Manager Home page.')
def logged_into_manager_page(context):
    time.sleep(.5)
    title = context.driver.title
    assert title == "Manager Home"




# TO SUBMIT A NEW STATUS ON A REIMBURSEMENT
@Given(u'the manager is on the manager home page.')
def on_manager_home_page(context):
    context.driver.get("file:///C:/Users/kckar/Desktop/Revature/project1_reimbursements/front-end/manager-home.html")


@When(u'the manager clicks on the submit reimbursement status tab.')
def select_status_change_tab(context):
    context.employee_page.click_status_reimbursement_tab().click()


@When(u'the manager inputs 3 in the reimbursement id input.')
def fill_reimburse_id_input(context):
    context.employee_page.select_reimburse_id_input().send_keys("3")


@When(u'the manager selects Denied from the drop down options.')
def select_option_dropdown(context):
    context.employee_page.select_option_input().click()


@When(u'the manager inputs not office supplies into the reason input.')
def fill_reason_input(context):
    context.employee_page.select_reason_input().send_keys("not office supplies")


@When(u'the manager clicks the submit status button.')
def select_submit_status(context):
    context.employee_page.click_submit_status_button().click()


@Then(u'the status will be submitted and the manager will be on the Manager Home page.')
def show_status_result_on_manager_page(context):
    time.sleep(.5)
    title = context.driver.title
    assert title == "Manager Home"




# # TO VIEW ALL REIMBURSEMENT REQUESTS
@When(u'the manager clicks on the view all reimbursements tab.')
def select_view_all_reimburse_tab(context):
    context.employee_page.click_all_reimbursements_tab().click()

@Then(u'the reimbursements will show and the manager will be on the Manager Home page.')
def view_reimburse_on_manager_page(context):
    time.sleep(.5)
    title = context.driver.title
    assert title == "Manager Home"





# TO VIEW REIMBURSEMENT STATISTICS
@When(u'the manager clicks the view reimbursement statistics tab.')
def step_impl(context):
    context.employee_page.click_reimbursement_statistics_tab().click()


@When(u'the manager selects the Count option from the dropdown.')
def click_statistic_option(context):
    context.employee_page.select_statistic_option().click()


@When(u'the manager clicks the statistics submit button.')
def select_statistics_submit_button(context):
    context.employee_page.click_statistic_submit_button().click()


@Then(u'the statistics are shown and the manager is on the Manager Home page.')
def show_statistics_on_manager_page(context):
    time.sleep(.5)
    title = context.driver.title
    assert title == "Manager Home"





# TO LOG OUT
@When(u'the manager clicks on the logout button.')
def select_manager_logout_button(context):
    context.employee_page.click_manager_logout_button().click()


@Then(u'the manager is redirected to the Home page.')
def redirect_manager_to_home(context):
    assert context.driver.title == "Home"
