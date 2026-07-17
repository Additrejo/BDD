import sys
from pathlib import Path

from behave import given, when, then

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))
from calculator import Calculator  # noqa: E402


@given("I have a calculator")
def step_given_calculator(context):
    context.calculator = Calculator()
    context.error = None


@when("I add {a:d} and {b:d}")
def step_when_add(context, a, b):
    context.result = context.calculator.add(a, b)


@when("I subtract {b:d} from {a:d}")
def step_when_subtract(context, a, b):
    context.result = context.calculator.subtract(a, b)


@when("I multiply {a:d} and {b:d}")
def step_when_multiply(context, a, b):
    context.result = context.calculator.multiply(a, b)


@when("I divide {a:d} by {b:d}")
def step_when_divide(context, a, b):
    try:
        context.result = context.calculator.divide(a, b)
    except ZeroDivisionError as e:
        context.error = e


@then("the result should be {expected:d}")
def step_then_result(context, expected):
    assert context.result == expected, (
        f"Expected {expected}, got {context.result}"
    )


@then("I should get a division by zero error")
def step_then_division_error(context):
    assert context.error is not None, "Expected a ZeroDivisionError but none was raised"