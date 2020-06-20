import turtle


# square
def square():
  qazi_turtle = turtle.Turtle()
  qazi_turtle.forward(100)
  qazi_turtle.right(90)
  qazi_turtle.forward(100)
  qazi_turtle.right(90)
  qazi_turtle.forward(100)
  qazi_turtle.right(90)
  qazi_turtle.forward(100)
#square()


elephant_weight = 3000
ant_weight = 0.2
qazi_turtle = turtle.Turtle()

if elephant_weight < ant_weight:
  square()
else:
  qazi_turtle.forward(200)


