import turtle
t = turtle.Turtle()
for i in range (180):
  t.speed(0)
  t.color('#FA8072')
  t.circle(190 - i, 90)
  t.left(90)
  t.color('	#EE82EE')
  t.circle(190 - i, 90)
  t.left(18)