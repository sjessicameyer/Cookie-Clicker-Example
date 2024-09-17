import turtle, time, threading
import os
from replit import audio
  
sc = turtle.Screen()
sc.setup(1.0, 1.0)
sc.bgcolor("#4054ed")
sc.title("An Outstanding Oreo Clicker")
sc.tracer(0)

sc.register_shape("cookie.gif")
cookie = turtle.Turtle()
cookie.shape("cookie.gif")
cookie.speed(0)

sc.register_shape("bronze_cursor_shop.gif")
bcs = turtle.Turtle()
bcs.shape("bronze_cursor_shop.gif")
bcs.up()
bcs.goto(-150, -150)

pen = turtle.Turtle()
pen.ht()
pen.color("white")
pen.up()
pen.goto(0, 100)

score = 0
cursorCounter = 0
cursorPrice = 10
def clicked(x, y):
  global score
  score += 1

cookie.onclick(clicked)

def bcs_clicked(x, y):
  global cursorPrice
  global cursorCounter
  global score
  if score >= cursorPrice:
    cursorCounter += 1
    score -= cursorPrice
    cursorPrice += 10
    
bcs.onclick(bcs_clicked)

while True:
  time.sleep(0.05)
  score += cursorCounter*.1
  pen.clear()
  pen.write(f"Crumbles: {score:.0f}", align="center", font=("Courier New", 20, "normal"))
  sc.update()
  