# Meu primeiro projeto em python 3
# Baseado no Snake Game de @TokyoEdTech

import turtle
import time
import random

delay = 0.1

# Pontuação
pontos = 0
recorde = 0

# Montando a Tela
tela = turtle.Screen()
tela.title("Snake")
tela.bgcolor("green")
tela.setup(width=800, height=600)
tela.tracer(0)

# Cabeça da cobra
cobra = turtle.Turtle()
cobra.speed(0)
cobra.shape("square")
cobra.color("red")
cobra.penup()
cobra.goto(0,0)
cobra.direction = "stop"

# Comida da Cobra
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("brown")
comida.penup()
comida.goto(0,100)

corpo = []

# Fonte
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Pontos: 0 Recorde: 0", align="center", font=("Arial", 12, "normal"))

# Funções
def subir():
    if cobra.direction != "down":
        cobra.direction = "up"

def descer():
    if cobra.direction != "up":
        cobra.direction = "down"

def direita():
    if cobra.direction != "left":
        cobra.direction = "right"

def esquerda():
    if cobra.direction != "right":
        cobra.direction = "left"

# Movimentação da cobra
def movimento():
    if cobra.direction == "up":
        y = cobra.ycor()
        cobra.sety(y + 20)

    if cobra.direction == "down":
        y = cobra.ycor()
        cobra.sety(y - 20)

    if cobra.direction == "left":
        x = cobra.xcor()
        cobra.setx(x - 20)

    if cobra.direction == "right":
        x  = cobra.xcor()
        cobra.setx(x + 20)

# Atalhos do teclado
tela.listen()
tela.onkeypress(subir, "w")
tela.onkeypress(descer, "s")
tela.onkeypress(esquerda, "a")
tela.onkeypress(direita, "d")

# Loop Principal
while True:
    tela.update()

    # Colisão com a comida
    if cobra.distance(comida) < 20:
            
        # Mover a comida pra uma posição aleatória
        x = random.randint(-390, 390)
        y = random.randint(-290, 290)
        comida.goto(x,y)

        # Adicionar corpo
        nova_parte = turtle.Turtle()
        nova_parte.speed(0)
        nova_parte.shape("square")
        nova_parte.color("grey")
        nova_parte.penup()
        corpo.append(nova_parte)

        # Aumentar a velocidade da cobra
        delay -= 0.02

        # Aumentar a pontuação
        pontos += 1

        if pontos > recorde:
                recorde = pontos

        pen.clear()
        pen.write("Pontos: {} Recorde: {}".format(pontos, recorde),align="center", font=("Arial", 12, "normal"))
    
    # Colisão com a borda
    if cobra.xcor()>390 or cobra.xcor()<-390 or cobra.ycor()>290 or cobra.ycor()<-290:
        time.sleep(1)
        cobra.goto(0,0)
        cobra.direction = "stop"

        for parte_corpo in corpo:
            parte_corpo.goto(1000,1000)

        # Resetar o corpo
        corpo.clear()

        # Resetar a pontuação
        pontos = 0

        # Resetar a velocidade
        delay = 0.1

        pen.clear()
        pen.write("Pontos: {} Recorde: {}".format(pontos, recorde), align="center", font=("Arial", 12, "normal"))

    

    for index in range(len(corpo)-1, 0, -1):
        x = corpo[index-1].xcor()
        y = corpo[index-1].ycor()
        corpo[index].goto(x, y)

    if len(corpo) > 0:
        x = cobra.xcor()
        y = cobra.ycor()
        corpo[0].goto(x, y)

    movimento()

    # Checagem de colisão com o próprio corpo
    for parte_corpo in corpo:
        if parte_corpo.distance(cobra) < 20:
            time.sleep(1)
            cobra.goto(0,0)
            cobra.direction = "stop"

            # Apagar o corpo
            for parte_corpo in corpo:
                parte_corpo.goto(1000,1000)

            # Deletar o corpo da cobra
            corpo.clear()

            # Resetar a pontuação
            pontos = 0

            # Resetar a velocidade da cobra
            delay = 0.1

            # Atualizar o display de pontuação
            pen.clear()
            pen.write("Pontos: {} Recorde: {}".format(pontos, recorde), align="center", font=("Arial", 12, "normal"))

    time.sleep(delay)

tela.mainloop()