from behave import given, when, then
from counter import Counter


@given("a new counter")
def step_new_counter(context):
    context.counter = Counter()


@when("I increment the counter")
def step_increment(context):
    context.counter.increment()


@when("I reset the counter")
def step_reset(context):
    context.counter.reset()


@then("the counter value should be {expected:d}")
def step_check_value(context, expected):
    assert context.counter.value == expected, (
        f"Expected {expected}, got {context.counter.value}"
    )