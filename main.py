import turtle
import random

screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catch the Turtle")
FONT = ('Ariel',20,'normal')
GRID_SIZE = 10
score = 0
game_over = False
turtle_list = []
COLOR = ["red","blue","green","purple","black","yellow","pink","gray"]


score_turtle = turtle.Turtle()


countdown_turtle = turtle.Turtle()

def setup_score_turtle():
    score_turtle.hideturtle()  #turtle ı gizleme
    score_turtle.color("dark blue") #yazıyı renklendrime
    score_turtle.penup()  # çizgi çekmemesi için

    top_height = screen.window_height()/2  # bu komut ekranın yüksekliğidir
    y = top_height *0.9  # ekranın yarısından itibaren başladığı için yarısının yüzde 90 ını aldık
    score_turtle.setpos(0,y)  #y koordinatına verdik
    score_turtle.write(arg="Score:0", move=False, align="center", font=FONT) # score yazısı yazma


def make_turtle(x,y):
    t = turtle.Turtle()

    def handle_click(x,y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg=f"Score:{score}", move=False, align="center", font=FONT)
    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2,2)
    t.color(random.choice(COLOR))
    t.goto(x*GRID_SIZE,y*GRID_SIZE)
    turtle_list.append(t)

x_coordinates =[-20,-10,0,10,20]
y_coordinates =[-20,-10,0,10,20]


def setup_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x,y)


def hide_turtles():
    for t in turtle_list:
        t.hideturtle()



def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_randomly,500)

def countdown(time):
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.color("red")
    countdown_turtle.penup()

    top_height = screen.window_height()/2
    y = top_height *0.9
    countdown_turtle.setpos(0,y-30)
    countdown_turtle.clear()
    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg=f"Time:{time}", move=False, align="center", font=FONT)
        screen.ontimer(lambda: countdown(time-1),1000)
    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="Game Over!", move=False, align="center", font=FONT)


turtle.tracer(0)



setup_score_turtle()
setup_turtles()
hide_turtles()
show_turtles_randomly()
countdown(10)
turtle.tracer(1)



turtle.mainloop()

