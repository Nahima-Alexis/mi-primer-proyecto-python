import turtle

# 1. Limpieza y configuración total de la ventana
try:
    turtle.clearscreen() # Borra cualquier intento fallido anterior
except:
    pass

ventana = turtle.Screen()
ventana.bgcolor("#0a0a0a")  # Fondo negro profundo
ventana.title("Rosa Perfecta en Turtle")
ventana.setup(width=650, height=650)

# 2. Configuración de la tortuga
t = turtle.Turtle()
t.hideturtle()             # Ocultamos la flecha desde el inicio para evitar bugs
t.speed(0)                 # Velocidad máxima

# DESACTIVAR ANIMACIÓN (Evita que VS Code se congele o se rompa)
ventana.tracer(0)

# ---- DIBUJO DE LOS PÉTALOS ----
t.penup()
t.goto(0, 40)              # Centrar el botón de la rosa
t.pendown()

# Dibujamos espirales concéntricas con tonos rojos
for i in range(120):
    # Alterna colores para darle un sombreado hermoso a los pétalos
    if i % 2 == 0:
        t.pencolor("#ff1a40")  # Rojo brillante
    else:
        t.pencolor("#99001a")  # Rojo oscuro / vino
        
    t.width(i // 30 + 1)       # El grosor aumenta hacia afuera
    t.forward(i * 1.2)
    t.right(61)                # Ángulo matemático perfecto para formar la rosa

# ---- DIBUJO DEL TALLO Y HOJA ----
t.penup()
t.goto(0, -10)
t.setheading(270)          # Apuntar la tortuga hacia abajo directamente
t.pendown()
t.pencolor("#228b22")      # Verde bosque
t.width(5)

# Tallo largo y estilizado
t.forward(180)

# Hoja lateral rápida
t.width(2)
t.fillcolor("#1e5631")
t.begin_fill()
t.left(45)
t.circle(50, 90)
t.left(90)
t.circle(50, 90)
t.end_fill()

# ---- MOSTRAR DIBUJO ----
ventana.update()           # Fuerza a la pantalla a mostrar la rosa terminada de golpe

# Línea final obligatoria para que la ventana se quede abierta fija
ventana.mainloop()
