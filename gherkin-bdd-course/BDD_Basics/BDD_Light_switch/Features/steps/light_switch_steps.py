from behave import given, when, then
from light_switch import LightSwitch


@given("a new light switch")
def step_new_switch(context):
    context.switch = LightSwitch()


@when("I toggle the switch")
def step_toggle(context):
    context.switch.toggle()


@then("the light should be on")
def step_light_on(context):
    assert context.switch.is_on is True


@then("the light should be off")
def step_light_off(context):
    assert context.switch.is_on is False