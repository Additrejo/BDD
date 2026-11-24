from behave import given, when, then
from semaforo import Semaforo


@given("un semáforo nuevo")
def paso_semaforo_nuevo(context):
    context.semaforo = Semaforo()


@when("el semáforo avanza")
def paso_avanzar(context):
    context.semaforo.avanzar()


@then('el color debe ser "{esperado}"')
def paso_verificar_color(context, esperado):
    assert context.semaforo.color == esperado, (
        f"Se esperaba '{esperado}', pero es '{context.semaforo.color}'"
    )


@then("los autos pueden avanzar")
def paso_autos_avanzan(context):
    assert context.semaforo.pueden_avanzar_autos() is True


@then("los autos no pueden avanzar")
def paso_autos_no_avanzan(context):
    assert context.semaforo.pueden_avanzar_autos() is False