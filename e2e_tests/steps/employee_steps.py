from behave import Given, When, Then
from e2e_tests.page_object_models.employee_portal import EmployeePage



# STEPS TO LOG IN
@Given(u'the employee is on the login page')
def get_reimbursement_login_page(context):
    EmployeePage.driver.get("http://127.0.0.1:5500/index.html")


@When(u'the employee types their username into the username input')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the employee types their username into the username input')


@When(u'the employee types their password into the password input')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the employee types their password into the password input')


@When(u'the employee clicks on the login button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the employee clicks on the login button')


@Then(u'the employee is redirected to the employee portal home page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the employee is redirected to the employee portal home page')



# STEPS TO REQUEST NEW REIMBURSEMENT
@Given(u'the employee is on the employee portal home page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the employee is on the employee portal home page')


@When(u'the employee clicks the new reimbursement tab')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the employee clicks the new reimbursement tab')


@When(u'the employee types the reason into the reason input')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the employee types the reason into the reason input')


@When(u'the employee types the amount into the amount input')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the employee types the amount into the amount input')


@When(u'the employee clicks the submit button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the employee clicks the submit button')


@Then(u'a success message will populate')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then a success message will populate')



# STEPS TO VIEW PENDING REIMBURSEMENTS
@When(u'the employee clicks the Pending reimbursements tab')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the employee clicks the Pending reimbursements tab')


@Then(u'the Pending reimbursements will populate')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the Pending reimbursements will populate')



# STEPS TO VIEW APPROVED REIMBURSEMENTS
@When(u'the employee clicks the Approved reimbursements tab')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the employee clicks the Approved reimbursements tab')


@Then(u'the Approved reimbursements will populate')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the Approved reimbursements will populate')



# STEPS TO VIEW DENIED REIMBURSEMENTS
@When(u'the employee clicks the Denied reimbursements tab')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the employee clicks the Denied reimbursements tab')


@Then(u'the Denied reimbursements will populate')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the Denied reimbursements will populate')



# STEPS TO LOG OUT
@When(u'the employee clicks the log out tab')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the employee clicks the log out tab')


@Then(u'the employee will be redirected to the login page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the employee will be redirected to the login page')
