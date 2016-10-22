import turtle

turtle.shape("turtle")

'''
#노가다

turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)


#좀 편함

for i in range(4):
    turtle.forward(100)
    turtle.right(90)
    
#더 편함
    
def drawRec(size):
  for i in range(4):
    turtle.forward(size)
    turtle.right(90)
'''
#ㄹㅇ 개편함


def drawSomething(size,angle):
  for i in range(angle):
    turtle.forward(size)
    turtle.right(360/angle)

drawSomething(100, 5)
drawSomething(200, 6)
drawSomething(10, 100)
    
