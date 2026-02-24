import turtle

# Crear la ventana
pantalla = turtle.Screen()
pantalla.title("Texto con Turtle")

# Crear la tortuga
t = turtle.Turtle()
t.speed(1)

# Ocultar la tortuga
t.hideturtle()

# Escribir texto
t.penup()
t.goto(0, 0)
t.write("Prueba1", align="center", font=("Arial", 24, "bold"))

# Mantener la ventana abierta hasta hacer clic
pantalla.exitonclick()
