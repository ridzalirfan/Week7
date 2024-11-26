from behave import *
from calculator import add, subtract, multiply, divide  # Importing calculator functions

# Background step to initialize the calculator
@given('the calculator is initialised')
def step_given_calculator_initialised(context):
    # This step could initialize the calculator if needed, 
    # but it's implied to be ready for each scenario.
    # context.calculator = True
    context.result = None

# Scenario: Addition
@when('I add {num1:d} and {num2:d}')
def step_when_add(context, num1, num2):
    context.result = add(num1, num2)

@then('the result should be {expected_result:d}')
def step_then_add_result(context, expected_result):
    assert context.result == expected_result, f"Expected {expected_result}, but got {context.result}"

# Scenario: Subtraction
@when('I subtract {num2:d} from {num1:d}')
def step_when_subtract(context, num1, num2):
    context.result = subtract(num1, num2)

@then('the result should be {expected_result:d}')
def step_then_subtract_result(context, expected_result):
    assert context.result == expected_result, f"Expected {expected_result}, but got {context.result}"

# Scenario: Multiplication
@when('I multiply {num1:d} and {num2:d}')
def step_when_multiply(context, num1, num2):
    context.result = multiply(num1, num2)

@then('the result should be {expected_result:d}')
def step_then_multiply_result(context, expected_result):
    assert context.result == expected_result, f"Expected {expected_result}, but got {context.result}"

# Scenario: Division
@when('I divide {num1:d} by {num2:d}')
def step_when_divide(context, num1, num2):
    context.result = divide(num1, num2)

@then('the result should be {expected_result:d}')
def step_then_divide_result(context, expected_result):
    assert context.result == expected_result, f"Expected {expected_result}, but got {context.result}"
