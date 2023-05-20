a = 0
img = 0
img1 = 0
img2 = 0
img3 = 0
def setup():
    global a,img, img1, img2, img3 
    size(600,450)
    img = loadImage("s.jpg")
    img1 = loadImage("hz.jpg")
    img2 = loadImage("go.jpg")
    img3 = loadImage("cvet.jpg")

    
def draw():
    global img,img1,img2,img3, a 
    rect (540,240,200,170)

    
    fill(250,20,20)
    rect(550,250,60,50)
    
    fill(237,218,7)
    rect(550,300,60,50)
    
    fill(50,214,78)
    rect(550,350,60,50)
    
    image(img3,400,100,100,150)
    
    
def mouseClicked():
    
    global a,img, img1 , img2
    
    
    if  mouseX > 550 and mouseX < 610 and mouseY > 250 and mouseY < 300:
        
        
        image(img,0,0,300,150)
        
        
    if mouseX > 550 and mouseX < 610 and mouseY > 300 and mouseY < 350:
        
    
        image(img1,0,150,300,150)
        
    if mouseX > 550 and mouseX < 610 and mouseY > 350 and mouseY < 400:
        
        
        image(img2,0,300,300,150)
    

    
