import turtle

# 1. Configuración de la pantalla
ventana = turtle.Screen()
ventana.bgcolor("black")       # Fondo negro para que los colores resalten
ventana.title("Círculos de Colores")

# 2. Configuración de la tortuga
t = turtle.Turtle()
t.speed(0)                    # Velocidad máxima de dibujo
t.width(2)                    # Grosor de la línea

# Lista con los colores que usará el dibujo
colores = ["red", "magenta", "blue", "cyan", "green", "yellow"]

# 3. Dibujo del patrón de círculos
for i in range(60):           # Dibujará 60 círculos en total
    color_actual = colores[i % 6]  # Va rotando entre los 6 colores de la lista
    t.pencolor(color_actual)
    
    t.circle(100)             # Dibuja un círculo de 100 pasos de radio
    t.right(6)                # Gira 6 grados a la derecha antes del siguiente círculo

# Ocultar la tortuga al terminar para que solo se vea el dibujo
t.hideturtle()

# Mantener la ventana abierta
ventana.mainloop()
