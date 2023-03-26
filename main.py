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
    player_img = p5.loadImage('player.png')  # load image data to player
    
    def draw(self):
        global program_state

        if (program_state == 'start'or program_state == 'play' or program_state == 'gameover'):
            p5.image(self.player_img, self.x, self.y)

class Iceberg:
    x = 0
    y = 0
    ib_1 = p5.loadImage('ib_1.png') 

    def draw(self):
        global program_state
        
        if (program_state == 'start'):
            p5.image(ib_1, slef.x, self,y)
           

def setup():
    p5.createCanvas(300, 300) 
    print('finished setup') 
    
def draw():
    p5.background(255) 
    p5.image(bg, 0, 0, bg.width*0.15, bg.height*0.15)
    player.draw()

    if (program_state == 'start'):
        p5.textFont(font)
        p5.textSize(20)
        p5.text('Arctic Voyage', 46, 115)
        p5.textSize(10)
        p5.text('press any key to start!', 40,130) 
     
    elif (program_state == 'play'):
        p5.fill(255)
         

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
