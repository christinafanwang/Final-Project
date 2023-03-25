import js
p5 = js.window

#images
bg = p5.loadImage('bg.png')  # load image data to bg
player = p5.loadImage('player.png')  # load image data to player
ib1 = p5.loadImage('ib_1.png') #iceberg 1
ib2 = p5.loadImage('ib_2.png') #iceberg_2
ib3 = p5.loadImage('ib_3.png') #iceberg_3

#load font
font = p5.loadFont('PressStart2P.otf')  # load font data to font

class Player:  
    x = 0  # set x at 0
    y = 0  # set y at 0
    def draw(self):
        p5.image(player, 105, 175, player.width*0.05, player.height*0.05)  
        
    

    def __init__(self, x, y, distance_x, distance_y):
        self.x = x  # initialize attribute x 
        self.y = y  # initialize attribute y 
        self.distance_x = distance_x
        self.distance_y = distance_y

player = Player(150,150)
def setup():
    p5.createCanvas(300, 300)   

def draw():
    p5.background(255)
    p5.image(bg, 0, 0, bg.width*0.15, bg.height*0.15)
    

def keyPressed(event):
    if(300 > player and player > 0):
        if(p5.keyCode == p5.RIGHT_ARROW):
           print('move point 10 pixels to the right..')
           player.move_player(10, 0)
        if(p5.keyCode == p5.LEFT_ARROW):
            print('move point 10 pixels to the left..')
            player.move_player(-10, 0)

    if(0 >= player):
        if(p5.keyCode == p5.RIGHT_ARROW):
            print('move point 10 pixels to the right..')
            player.move_player(10, 0) 

    if(300 <= player):
        if(p5.keyCode == p5.LEFT_ARROW):
            print('move point 10 pixels to the left..')
            player.move_player(-10, 0)  

def keyReleased(event):
    pass

def mousePressed(event):
    pass

def mouseReleased(event):
    pass
