# a131_final_project_ar.py

import turtle as tt
import random as rng

# Quick Values

tcolor = "White"
tshape = "circle"
tt.bgcolor("Black")
tfont = ("Roboto", 20, "normal")
tsize = 4
score = 0
timer = 60
count = 1000
timer_up = False

# Shape Setup For Game

circle = tt.Turtle()
circle.color(tcolor)
circle.shapesize(tsize)
circle.shape(tshape)
circle.pu()
tc = tt.Turtle()
tc.color("White")
tc.pu()
tc.goto(-190, 140)
tc.hideturtle()
score_display = tt.Turtle()
score_display.pu()
score_display.goto(190, 140)
score_display.color("White")
score_display.hideturtle()

# Title

te = tt.Turtle()
te.goto(0,300)
te.color("white")
te.write("Perfect Aim Game", font=tfont, align='center')
te.pu()

# Find Game Difficulty

difficultylist = ["Easy", "Hard"]

print("Difficulties:", difficultylist)
while True:
    difficulty = input("Select a Difficulty:")
    if difficulty in difficultylist:
        break
    else:
        print("Invalid Difficulty (Case Sensitive)")

if difficulty == "Easy":
    print("Easy Mode")
    te.goto(0,-300)
    te.color("white")
    te.write("Easy Mode", font=tfont, align='center')
if difficulty == "Hard":
    print("Hard Mode")
    te.goto(0,-300)
    te.color("white")
    te.write("Hard Mode", font=tfont, align='center')

# Begin ACTUAL Game Functions
score_display = tt.Turtle()
score_display.pu()
score_display.goto(190, 140)
score_display.color("White")
score_display.hideturtle()
score_display.speed(50)

#SCORE TO TELL PLAYER HOW MUCH THEY GOT:
def update_score():
    global score
    score += 1000
    score_display.clear()
    score_display.write("Score: " + str(score), font=tfont)

#TIMER FOR PLAYER AND WHEN GAME ENDS
def countdown():
  global timer, timer_up
  tc.clear()
  if timer <= 0:
    tc.write("Time's Up", font=tfont)
    timer_up = True
  else:
    tc.write("Timer: " + str(timer), font=tfont)
    timer -= 1
    tc.getscreen().ontimer(countdown, count)

#When Circle Is Clicked During Easy Mode
def when_clicked_easy(i, j):
    global timer, tsize
    if (timer_up == False) and difficulty == "Easy":
        circle.color("Black")
        circle.stamp()
        circle.color(tcolor)
        circle.shapesize(tsize)
        update_score()
        change_position_easy()
    else:
        circle.hideturtle()

#Easy Mode Position Change
def  change_position_easy():
    pickside = rng.randint(1,4)
    if pickside == 1:
        circle.goto(150,0)
    if pickside == 2:
        circle.goto(-150,0)
    if pickside == 3:
        circle.goto(0,150)
    if pickside == 4:
        circle.goto(0,-150)

#When Circle Is Clicked During Hard Mode
def when_clicked_hard(i, j):
    global timer, tsize
    if (timer_up == False) and difficulty == "Hard":
        circle.color("Black")
        circle.stamp()
        circle.color(tcolor)
        circle.shapesize(tsize)
        update_score()
        change_position_hard()
    else:
        circle.hideturtle()

#Hard Mode Position Change
def  change_position_hard():
    pickside = rng.randint(1,8)
    if pickside == 1:
        circle.goto(100,0)
    if pickside == 2:
        circle.goto(-100,0)
    if pickside == 3:
        circle.goto(0,100)
    if pickside == 4:
        circle.goto(0,-100)
    if pickside == 5:
        circle.goto(200,0)
    if pickside == 6:
        circle.goto(-200,0)
    if pickside == 7:
        circle.goto(0,200)
    if pickside == 8:
        circle.goto(0,-200)

#GAME BEGINS
#EASY CLICK
if difficulty == "Easy":
    circle.onclick(when_clicked_easy)
#HARD CLICK
if difficulty == "Hard":
    circle.onclick(when_clicked_hard)

#CONTINUES GAME UNTIL INEVITABLE DEATH
wn = tt.Screen()
wn.ontimer(countdown, count) 
wn.mainloop()