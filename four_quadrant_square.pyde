def setup():
    size(500,500)
    
def draw():
    background(0,0,255)
    noStroke()
    fill(255,0,0)
    
    if mouseX < width / 2 and mouseY < height / 2:
        rect(0,0, width / 2, height / 2)
    elif mouseX > width / 2 and mouseY < height / 2:
        rect(width / 2,0, width / 2, height / 2)
    elif mouseX < width / 2 and mouseY > height / 2:
        rect(0,height / 2, width / 2, height / 2)
    else:
        rect(width / 2, height / 2, width / 2, height / 2)
       
   #rollover 
    bw = width + 0.3
    bh = height + 0.3
    left = (width - (bw)) / 2
    top = (height - (bh)) / 2
    
    if mouseX > left and mouseX < left + bw and mouseY > top and mouseY < top + bh:
        fill(30,255,255)
    else:
        fill(90,255,255)
    
    
    rect(left,top,bw,bh)
        
