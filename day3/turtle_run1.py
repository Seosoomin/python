import turtle as t

wn = t.Screen()
wn.bgcolor("lightgreen")
wn.title("Turtle Run Ver.1")



def speedupMove():
  move = move + 10
    
def speeddownMove():
  move = move - 10

def turn_right():
  t.setheading(0)      # 거북이의 머리 방향을 0도 돌린다.
  t.forward(10)

def turn_left():
  t.setheading(180)    # 거북이의 머리 방향을 180도 돌린다.
  t.forward(10)

def turn_up():
  t.setheading(90)   
  t.forward(10)

def turn_down():
  t.setheading(270)
  t.forward(10)

def reset():
  t.clear()            # 화면을 리셋

def up():
  t.penup()

def down():
  t.pendown()

t.shape("turtle")
t.speed(0)
t.color("red","black")
t.onkeypress(turn_right, "Right") # 오른쪽 방향키가 눌리면 turn_right 함수 수행
t.onkeypress(turn_left, "Left")   # 왼쪽 방향키가 눌리면 turn_left 함수 수행
t.onkeypress(turn_up, "Up")       # 위쪽 방향키가 눌리면 turn_up 함수 수행
t.onkeypress(turn_down, "Down")   # 아래쪽 방향키가 눌리면 turn_down 함수 수행
t.onkeypress(reset, "r")     # R키가 눌리면 reset 함수 수행
t.onkeypress(up, "q")
t.onkeypress(down, "w")
t.onkeypress(speedupMove, "a")
t.listen()                        # 입력을 기다림...



