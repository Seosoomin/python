import turtle as t

wn = t.Screen()
wn.bgcolor("lightgreen")
wn.title("Turtle Run Ver.1")

t.shape("turtle")
t.color("gray")

b = t.Turtle()  # 악당
c = t.Turtle()  # 먹이
b.shape("turtle")
c.shape("circle")
b.color("red")   # 악당 빨간색
c.color("green") # 먹이 초록색
b.color("red")   # 악당 빨간색
c.color("green") # 먹이 초록색
b.up()
b.goto(0, 200)  # 위 방향으로 200 이동
c.up()
c.goto(0, -200) # 아래 방향으로 200 이동


move = 10   # 주인공의 이동거리

def moveup():
  global move
  move = move + 1
    
def movedown():
  global move
  move = move - 1

def turn_right():
  t.setheading(0)      # 거북이의 머리 방향을 0도 돌린다.
  t.forward(move)
  run()
  trace()

def turn_left():
  t.setheading(180)    # 거북이의 머리 방향을 180도 돌린다.
  t.forward(move)
  run()
  trace()

def turn_up():
  t.setheading(90)   
  t.forward(move)
  run()
  trace()

def turn_down():
  t.setheading(270)
  t.forward(move)
  run()
  trace()

def reset():
  t.clear()            # 화면을 리셋

def run():
  if c.pos()[0] >= 150:
     c.setheading(180)
  elif c.pos()[0] <= -150:
    c.setheading(0)
  c.forward(20)
  
def trace():
  angle = b.towards(t.pos())
  b.setheading(angle)
  b.forward(5)

t.speed(0)
t.penup()
t.onkeypress(turn_right, "Right") # 오른쪽 방향키가 눌리면 turn_right 함수 수행
t.onkeypress(turn_left, "Left")   # 왼쪽 방향키가 눌리면 turn_left 함수 수행
t.onkeypress(turn_up, "Up")       # 위쪽 방향키가 눌리면 turn_up 함수 수행
t.onkeypress(turn_down, "Down")   # 아래쪽 방향키가 눌리면 turn_down 함수 수행
t.onkeypress(reset, "r")     # R키가 눌리면 reset 함수 수행
t.onkeypress(moveup, "q")
t.onkeypress(movedown, "w")
t.listen()                        # 입력을 기다림...



