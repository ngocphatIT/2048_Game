import pygame,random
pygame.init()
font=pygame.font.SysFont("san",40)
font2=pygame.font.SysFont("san",25)
font1=pygame.font.SysFont("san",30)
screen_w=350
screen_h=350
d=50
number=5
size_img=50
screen=pygame.display.set_mode((screen_w,screen_h))
pygame.display.set_caption("2048")
data=[]
def remove2():
    for i in range (number):
        for j in range (number):
            if data[i][j]==2:
                data[i][j]=0
def create():
    data=[]
    for i in range (number):
        r=[0]*number
        data.append(r)
    count=0
    endloop=False
    for i in range (number):
        for j in range(number):
            data[i][j]=random.randint(-5,5)
            if data[i][j]<=0:
                data[i][j]=0
            else:
                count+=1
                if data[i][j]<=2:
                    data[i][j]=2
                else:
                    data[i][j]=4
            if count==number:
                endloop=True
                break
        if endloop:
            break
    return data
def checkgameover():
    for i in range(number):
        for j in range(number):
            if data[i][j]==0:
                return False
            if j+1<number:
                if data[i][j]==data[i][j+1]:
                    return False
            if j-1>=0:
                if data[i][j]==data[i][j-1]:
                    return False
            if i+1<number:
                if data[i][j]==data[i+1][j]:
                    return False
            if i-1>=0:
                if data[i][j]==data[i-1][j]:
                    return False
    return True
def goleft():
    for x in range(number):
        for y in range(number):
            if data[x][y]==0:
                for i in range (number-y):
                    if data[x][y+i]!=0 and i!=0:
                        data[x][y]=data[x][y+i]
                        try:
                            data[x][y+i]=0
                            break
                        except:
                            pass
    for x in range(number):
        for y in range(number-1):
            if data[x][y]==data[x][y+1]:
                data[x][y]+=data[x][y+1]
                data[x][y+1]=0
    for x in range(number):
        for y in range(number):
            if data[x][y]==0:
                for i in range (number-y):
                    if data[x][y+i]!=0 and i!=0:
                        data[x][y]=data[x][y+i]
                        try:
                            data[x][y+i]=0
                            break
                        except:
                            pass
def goright():
    for x in range(number):
        for y in range(number-1,-1,-1):
            if data[x][y]==0:
                for i in range (y+1):
                    if data[x][y-i]!=0 and i!=0:
                        data[x][y]=data[x][y-i]
                        try:
                            data[x][y-i]=0
                            break
                        except:
                            pass
    for x in range(number):
        for y in range(number-1,0,-1):
            if data[x][y]==data[x][y-1]:
                data[x][y]+=data[x][y-1]
                data[x][y-1]=0
    for x in range(number):
        for y in range(number-1,-1,-1):
            if data[x][y]==0:
                for i in range (y+1):
                    if data[x][y-i]!=0 and i!=0:
                        data[x][y]=data[x][y-i]
                        try:
                            data[x][y-i]=0
                            break
                        except:
                            pass
def goup():
    for x in range(number):
        for y in range(number):
            if data[x][y]==0:
                for i in range (number-x):
                    if data[x+i][y]!=0 and i!=0:
                        data[x][y]=data[x+i][y]
                        try:
                            data[x+i][y]=0
                            break
                        except:
                            pass
    for x in range(number-1):
        for y in range(number):
            if data[x][y]==data[x+1][y]:
                data[x][y]+=data[x+1][y]
                data[x+1][y]=0
    for x in range(number):
        for y in range(number):
            if data[x][y]==0:
                for i in range (number-x):
                    if data[x+i][y]!=0 and i!=0:
                        data[x][y]=data[x+i][y]
                        try:
                            data[x+i][y]=0
                            break
                        except:
                            pass
def godown():
    for x in range(number-1,-1,-1):
        for y in range(number):
            if data[x][y]==0:
                for i in range (x+1):
                    if data[x-i][y]!=0 and i!=0:
                        data[x][y]=data[x-i][y]
                        try:
                            data[x-i][y]=0
                            break
                        except:
                            pass
    for x in range(number-1,0,-1):
        for y in range(number):
            if data[x][y]==data[x-1][y]:
                data[x][y]+=data[x-1][y]
                data[x-1][y]=0
    for x in range(number-1,-1,-1):
        for y in range(number):
            if data[x][y]==0:
                for i in range (x+1):
                    if data[x-i][y]!=0 and i!=0:
                        data[x][y]=data[x-i][y]
                        try:
                            data[x-i][y]=0
                            break
                        except:
                            pass
def add(text):
    n=1
    number_add=random.randint(1,2)
    if text=="RIGHT" or text=='LEFT':
        if text=='RIGHT':
            y=0
        else:
            y=number-1
        for i in range(number_add):
            count=0
            while data[n][y]!=0:
                n=random.randint(0,number-1)
                count+=1
                if count==number*2:
                    break
            if count!=number*2:
                t= random.randint(0,9)
                if t>=0 and t<6:
                    t=1
                elif t>=6 and t<9:
                    t=2
                else:
                    t=3
                data[n][y]=2**t
    elif text=="UP" or text=="DOWN":
        if text=="DOWN":
            x=0
        else:
            x=number-1
        for i in range(number_add):
            count=0
            while data[x][n]!=0:
                n=random.randint(0,number-1)
                count+=1
                if count==number*2:
                    break
            if count!=number*2:
                t= random.randint(0,9)
                if t>=0 and t<6:
                    t=1
                elif t>=6 and t<9:
                    t=2
                else:
                    t=3
                data[x][n]=2**t
def draw():
    screen.fill((16,54,103))
    for i in range(number+1):
        pygame.draw.line(screen,(255,255,255),(d+i*size_img,d),(d+i*size_img,d+size_img*number),1)
        pygame.draw.line(screen,(255,255,255),(d,d+i*size_img),(d+size_img*number,d+i*size_img),1)
    for y, row in enumerate(data):
        for x, tile in enumerate(row):
            if tile!=0:
                screen.blit(pygame.transform.scale(pygame.image.load(f'img/{tile}.jpg'),(size_img-1,size_img-1)),(d+x*size_img+1,1+d+y*size_img))
run=True
new=False
gameover=False
data=create()
while run:
    draw()
    gameover=checkgameover()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.KEYDOWN :
            if not gameover:
                if event.key==pygame.K_LEFT:
                    goleft()
                    add('LEFT')
                if event.key==pygame.K_RIGHT:
                    goright()
                    add('RIGHT')
                if event.key==pygame.K_UP:
                    goup()
                    add("UP")
                if event.key==pygame.K_DOWN:
                    godown()
                    add('DOWN')
            if event.key==pygame.K_F2:
                data=create()
            if event.key==pygame.K_F12 and gameover:
                remove2()
    if gameover:
        screen.blit(font.render("GAME OVER",True,(0,0,0)),(d+int(size_img*0.85),int(d+size_img*2.25)))
        screen.blit(font2.render("Press F2 to restart",True,(255,25,55)),(d+int(size_img*1),int(d+size_img*2.85)))
    screen.blit(font1.render("Mode by Ngoc Phat",True,(255,255,255)),(d+int(size_img*0.75),d+int(size_img*5.25)))
    pygame.display.update()
pygame.quit()