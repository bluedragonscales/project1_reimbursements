from behave import Given, When, Then


# LOGGING IN
@Given(u'the employee is on the login page.')
def get_login_page(context):
    context.driver.get("file:///C:/Users/kckar/Desktop/Revature/project1_reimbursements/front-end/employee-home.html")


@When(u'the employee fills in the employee id.')
def fill_employee_id(context):
    raise NotImplementedError(u'STEP: When the employee fills in the employee id.')


@When(u'the employee fills in the password.')
def fill_employee_password(context):
    raise NotImplementedError(u'STEP: When the employee fills in the password.')


@When(u'the employee clicks the log in button.')
def select_login_button(context):
    context.employee_page.click_login_button().click()


@Then(u'the employee is redirected to the employee home page.')
def get_employee_home_page(context):
    title = context.driver.title
    assert title == "Employee Home"



# SUBMITTING A NEW REIMBURSEMENT REQUEST
@Given(u'the employee is on the employee home page.')
def get_employee_home_page(context):
    context.driver.get("file:///C:/Users/kckar/Desktop/Revature/project1_reimbursements/front-end/employee-home.html")


@When(u'the employee clicks the request reimbursement link')
def select_request_reimbursement_tab(context):
    context.employee_page.click_request_reimbursement_tab().click()


@When(u'the employee fills in the request purpose.')
def fill_request_purpose(context):
    raise NotImplementedError(u'STEP: When the employee fills in the request purpose.')


@When(u'the employee fills in the amount.')
def fill_amount(context):
    raise NotImplementedError(u'STEP: When the employee fills in the amount.')


@When(u'the employee clicks the submit button.')
def select_submit_reimbursement_button(context):
    context.employee_page.click_submit_reimbursement_button().click()


@Then(u'a new request is submitted.')
def request_submitted(context):
    title = context.driver.title
    assert title == "Employee Home"




# VIEWING EMPLOYEE'S REIMBURSEMENT REQUESTS
@Given(u'the employee is on the employee home page.')
def get_employee_home_page(context):
    context.driver.get("file:///C:/Users/kckar/Desktop/Revature/project1_reimbursements/front-end/employee-home.html")


@When(u'the employee clicks the view reimbursements button.')
def select_view_reimbursements_tab(context):
    context.employee_page.click_view_reimbursement_button().click()


@Then(u'the reimbursements are shown.')
def reimbursements_are_shown(context):
    title = context.driver.title
    assert title == "Employee Home"




# LOGGING OUT
@Given(u'the employee is on the employee home page.')
def get_employee_home_page(context):
    context.driver.get("file:///C:/Users/kckar/Desktop/Revature/project1_reimbursements/front-end/employee-home.html")

@When(u'the employee clicks on the log out button.')
def select_logout_button(context):
    context.employee_page.click_logout_button().click()


@Then(u'they will be logged out.')
def employee_is_logged_out(context):
    title = context.driver.title
    assert title == "Home"
