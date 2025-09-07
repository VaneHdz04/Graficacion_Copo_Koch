import turtle

def koch_curve(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_curve(t, length, level-1)
        t.left(60)
        koch_curve(t, length, level-1)
        t.right(120)
        koch_curve(t, length, level-1)
        t.left(60)
        koch_curve(t, length, level-1)

# Configuración de la ventana
screen = turtle.Screen()
screen.bgcolor("black")

# Configuración de la tortuga
t = turtle.Turtle()
t.speed(0)
t.color("cyan")

# Dibujar solo una curva (media parte del copo)
t.penup()
t.goto(-200, 0)
t.pendown()

nivel = 4   # Nivel de recursión (más alto = más detalle)
longitud = 400  # Longitud inicial

koch_curve(t, longitud, nivel)

turtle.done()
