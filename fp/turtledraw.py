# Exercise 5 on "How to think like a computer scientist", ch. 11.

import turtle

t = turtle.Turtle()

# Use t.up(), t.down() and t.goto(x, y)

# Put your code here
with open("C:/Users/cccri/OneDrive/Documentos/1semestre 1 ano/fp/Aulas/aula06/drawing.txt", "r") as cmds:
    for line in cmds:
        if line == "UP\n":
            t.up()
        elif line == "DOWN\n":
            t.down()
        else:
            t.goto(int(line.split()[0]), int(line.split()[1]))



# wait
turtle.Screen().exitonclick()

