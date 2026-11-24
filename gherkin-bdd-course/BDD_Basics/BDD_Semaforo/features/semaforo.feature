# language: es
Característica: Semáforo de tráfico
  Como conductor
  Quiero saber cuándo puedo avanzar
  Para cruzar el cruce de forma segura

  Escenario: El semáforo inicia en rojo
    Dado un semáforo nuevo
    Entonces el color debe ser "rojo"

  Escenario: Del rojo pasa a verde
    Dado un semáforo nuevo
    Cuando el semáforo avanza
    Entonces el color debe ser "verde"

  Escenario: Del verde pasa a amarillo
    Dado un semáforo nuevo
    Cuando el semáforo avanza
    Y el semáforo avanza
    Entonces el color debe ser "amarillo"

  Escenario: Del amarillo vuelve a rojo
    Dado un semáforo nuevo
    Cuando el semáforo avanza
    Y el semáforo avanza
    Y el semáforo avanza
    Entonces el color debe ser "rojo"

  Escenario: Los autos avanzan solo con luz verde
    Dado un semáforo nuevo
    Cuando el semáforo avanza
    Entonces los autos pueden avanzar

  Escenario: Los autos no avanzan con luz roja
    Dado un semáforo nuevo
    Entonces los autos no pueden avanzar