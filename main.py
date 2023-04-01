import js
p5 = js.window

program_state = 'start'
#bg image
bg = p5.loadImage('bg.png')  # load image data to bg
#set font
font = p5.loadFont('PressStart2P.otf')

class Player:  
    x = 0  # set x at 0
    y = 0  # set y at 0
    distance_x = 0
    distance_y = 0
    
    player_img = p5.loadImage('player.png')  # load image data to player
    
    def draw(self):
        p5.image(self.player_img, self.x, self.y)
            
    def move_player(self, distance_x, distance_y):
        self.x = self.x + distance_x
        self.y = self.y + distance_y
        
class Iceberg:
    x = 0
    y = 0
    speed = 0


    def __init__(self,x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        
class Big(Iceberg):
    ib_1 = p5.loadImage('ib_1.png')
    def draw(self):
        p5.image(self.ib_1, self.x, self.y)


class Medium(Iceberg):
    ib_2 = p5.loadImage('ib_2.png')
    def draw(self):
        p5.image(self.ib_2, self.x, self.y)

class Small(Iceberg):
    ib_3 = p5.loadImage('ib_3.png')
    def draw(self):
        p5.image(self.ib_3, self.x, self.y)

def setup():
    p5.createCanvas(300, 300) 
    print('finished setup') 

player = Player()    
ib_1 = Big(p5.random(1,300),0,0.5)
ib_2 = Medium(p5.random(1,300),0,0.5)
ib_3 = Small(p5.random(1,300),0,0.5)

def draw():
    p5.background(255) 
    p5.image(bg, 0, 0, bg.width*0.15, bg.height*0.15)
    player.draw()

    if (program_state == 'start'):
        p5.textFont(font)
        p5.textSize(20)
        p5.text('ARCTIC VOYAGE', 46, 115)
        p5.textSize(10)
        p5.text('click anywhere to start!', 40,130) 
     
    elif (program_state == 'play'):
        p5.fill(255)

    ib_1.draw()
    ib_2.draw()
    ib_3.draw()
    
    #dis = p5.dist(player.x , player.y , iceberg.x , iceberg.y)

    elif(dis <= 15):
        player.distance_x = 0
        player.distance_y = 0
        iceberg.distance_x = 0
        iceberg.distance_y = 0

        p5.fill(0)
        p5.textFont(font)
        p5.textSize(30)
        p5.text("TRY AGAIN",100,100)
        p5.textSize(20)
        p5.text("click anywhere to restart game")

def keyPressed(event): 
    global program_state
    
    if(program_state == 'start'):
    
    if (program_state =='play'):
        if(300 > player and player > 0):
            if(p5.keyCode == p5.RIGHT_ARROW):
                player.move_player(10, 0)
            if(p5.keyCode == p5.LEFT_ARROW):
                player.move_player(-10, 0)
        if(0 >= player):
            if(p5.keyCode == p5.RIGHT_ARROW):
                player.move_player(10, 0) 
        if(300 <= player):
            if(p5.keyCode == p5.LEFT_ARROW):
                player.move_player(-10, 0)   

def keyReleased(event):
    pass

def mousePressed(event):
    if(program_state == 'start'):
        program_state = 'play'

def mouseReleased(event):
    pass
