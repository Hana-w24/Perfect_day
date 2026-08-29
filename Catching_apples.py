import lucid as lu
from random import randint

def moveLeft(e):
    if bucket.x > 5:
        bucket.x -= 30

def moveRight(e):
    if bucket.x < 1160:
        bucket.x += 30

def dropApple(apple):
    apple.move(0,3)
    drop = win.after(80, lambda: dropApple(apple))
    x,y = apple.getXY()
    if y > 560:
        win.after_cancel(drop)
        apple.undraw()
        global score
        if bucket.x < x < bucket.x+100:
            score+=1
        else:
            score -= 1
            splat = lu.Image(win, x, y, "Images/apple2.png")
        scoreBox.setText("Score: " + str(score))



def createApple():
    tree = randint(1,2)
       
    if tree == 1:
        x = randint(150, 400)
        y = randint(100,230)
    else:
        x = randint(850, 1100)
        y = randint(100, 230)
    apple = lu.Image(win, x, y, "Images/apple.png")
    win.after(2000, lambda: createApple())
    win.after(1000, lambda: dropApple(apple))


   
win = lu.Window("Apple Game", 1260, 720)
win.bg = "skyblue"
ground = lu.Rectangle(win, 0, 400, 1280, 320)
ground.fill = "lawngreen"
ground.outline = "lawngreen"
tree1 = lu.Image(win, 280, 280, "Images/apple_tree.png")
tree2 = lu.Image(win, 980, 280, "Images/apple_tree.png")
bucket = lu.Rectangle(win, 640, 540, 100, 80)
bucket.fill = "brown"
score = 0
scoreBox = lu.Text(win, 645, 120, "Score: 0")
scoreBox.setProperties(font=("Arial", 32, "normal"))
win.bind_key('Left', moveLeft)
win.bind_key('Right', moveRight)

createApple()

# Keep the window open and process animations/keyboard input.
lu.tk.mainloop()

