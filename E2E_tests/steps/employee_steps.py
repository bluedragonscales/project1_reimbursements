from behave import Given, When, Then

@Given(u'the employee is on the login page.')
def get_login_page(context):
    raise NotImplementedError(u'STEP: Given the employee is on the login page.')


@When(u'the employee fills in the employee id.')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the employee fills in the employee id.')


@When(u'the employee fills in the password.')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the employee fills in the password.')


@When(u'the employee clicks the log in button.')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the employee clicks the log in button.')


@Then(u'the employee is redirected to the employee home page.')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the employee is redirected to the employee home page.')


@Given(u'the employee is on the submit request page.')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the employee is on the submit request page.')


@When(u'the employee fills in the request purpose.')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the employee fills in the request purpose.')


@When(u'the employee fills in the amount.')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the employee fills in the amount.')


@When(u'the employee clicks the submit button.')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the employee clicks the submit button.')


@Then(u'a new request is submitted.')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then a new request is submitted.')


@Given(u'the employee is on the employee home page.')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the employee is on the employee home page.')


@When(u'the employee clicks the view reimbursements button.')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the employee clicks the view reimbursements button.')


@Then(u'the reimbursements are shown.')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the reimbursements are shown.')


@When(u'the employee clicks on the log out button.')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the employee clicks on the log out button.')


@Then(u'they will be logged out.')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then they will be logged out.')