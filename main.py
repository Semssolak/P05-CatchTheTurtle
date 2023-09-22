import turtle
import random

screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catch the Turtle")
FONT = ('Ariel',20,'normal')  # yazılımda böyle sabit şeyler büyük harfle tanımlanmalıdır
GRID_SIZE = 10  #daha dar veya daha geniş bir alanda olmasını istersek bunu değiştirebiliriz
score = 0
game_over = False
turtle_list = [] #turtle list
COLOR = ["red","blue","green","purple","black","yellow","pink","gray"]

#score turtle
score_turtle = turtle.Turtle()

#countdown turtle
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
        #print(x,y) koordinatlarını almak isteseydik
        global score #skoru burada değiştirebilmemizi sağladı
        score += 1
        score_turtle.clear() #yazmadan önce önceki skoru temizlemeliyiz
        score_turtle.write(arg=f"Score:{score}", move=False, align="center", font=FONT)
    t.onclick(handle_click)  #tıklama işlemini sağlar
    t.penup()
    t.shape("turtle")
    t.shapesize(2,2)
    t.color(random.choice(COLOR))
    t.goto(x*GRID_SIZE,y*GRID_SIZE)  #ilerleme miktarı az olduğundan 10 la çarpılmış hallerini aldık
    turtle_list.append(t) # bütün turtle ları bu listeye attık

x_coordinates =[-20,-10,0,10,20]
y_coordinates =[-20,-10,0,10,20]


def setup_turtles():
    for x in x_coordinates: #burda belirtilen koordinatlarda bulunan kaplumbağalarla bir matrix yaptık
        for y in y_coordinates:
            make_turtle(x,y)


def hide_turtles(): #bütün turtle ları gizleme komutu
    for t in turtle_list:
        t.hideturtle()


#recursive function : bir fonksiyonun kendisini içinde çalıştırma
def show_turtles_randomly():
    if not game_over: # game over false sa çalışır 3)artık sonsuz kez çalışmıcak
        hide_turtles() #her seferinde gizlemek için , 2)hepsini gizlediğimiz için sonsuza kadar çalışır
        random.choice(turtle_list).showturtle()  # listeden birini seçer ve gösterir
        screen.ontimer(show_turtles_randomly,500) #1sn=1000
        # 1)burda kendi içinde çalıştırdığımız için tüm hepsi çıkana kadar çalıştıracak

def countdown(time): # üstteki skor yazısınının kodunun aynısı
    global game_over
    countdown_turtle.hideturtle()  #turtle ı gizleme
    countdown_turtle.color("red") #yazıyı renklendrime
    countdown_turtle.penup()  # çizgi çekmemesi için

    top_height = screen.window_height()/2  # bu komut ekranın yüksekliğidir
    y = top_height *0.9  # ekranın yarısından itibaren başladığı için yarısının yüzde 90 ını aldık
    countdown_turtle.setpos(0,y-30)  #y koordinatına verdik biraz altı
    countdown_turtle.clear() # her seferinde silinmesi için
    if time > 0:
        countdown_turtle.clear()  #her seferinde silinmesi için
        countdown_turtle.write(arg=f"Time:{time}", move=False, align="center", font=FONT) # score yazısı yazma
        screen.ontimer(lambda: countdown(time-1),1000)  #lambdayla fonksiyon içinde vermek daha iyi
        #on timer her saniye değişme fonksiyonu burada fonksiyonu içinde çağırdık süre her seferinde azalcak
    else:
        game_over = True #süre bittiğinde game over true çalışacak
        countdown_turtle.clear()
        hide_turtles() #tüm turtle ları da sileriz
        countdown_turtle.write(arg="Game Over!", move=False, align="center", font=FONT) # score yazısı yazma
        #ontimer ı if else de kullanıp else kısmında kullanmadığımızdan else girdiğinde sonlanacak

turtle.tracer(0) # ilerleme animasyonlarını sıfırladık dierk o konumlarda başlar turtle lar
#bu takip etmeyeyi bırakır


setup_score_turtle()
setup_turtles()
hide_turtles()
show_turtles_randomly()
countdown(10)
turtle.tracer(1) #buda takip etmeye başlar



turtle.mainloop()

