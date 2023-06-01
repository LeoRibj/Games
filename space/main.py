import pygame
import sys , os,time
import keyboard as kb
import random
from pygame.locals import *

pygame.init()
relogio = pygame.time.Clock()
largura,altura=800,600
tela = pygame.display.set_mode((largura,altura))
fundo = pygame.image.load(os.path.join("space","assets","img","espaco.jpg")).convert_alpha()
nave = pygame.image.load(os.path.join("space","assets","img","ship.png")).convert_alpha()
nave= pygame.transform.scale(nave,(100,80))
fundorec=fundo.get_rect(center=((largura/2,(altura/2))))
tiro= pygame.image.load(os.path.join("space","assets","img","laser.png")).convert_alpha()
meteoro= pygame.image.load(os.path.join("space","assets","img","meteor.png")).convert_alpha()
meteoro= pygame.transform.scale(meteoro,(70,70))


#tiro= pygame.transform.scale(tiro,(40,40))
tiro_estado="ready"
meteorocai="caindo"

bullets = []
meteoros=[]
fogos=[]
campof=[]

posy_y=500
posy_x=500

navrec= nave.get_rect(center=(posy_y,posy_x))

life = pygame.image.load(os.path.join("space","assets","img","ship.png")).convert_alpha()
life= pygame.transform.scale(nave,(30,20))
liferec= life.get_rect(center=(740,15))
campoforça = pygame.image.load(os.path.join("space", "assets","img","campo de força.png")) 
campoforça= pygame.transform.scale(campoforça,(130,100))
vidas=3

print(navrec)

font=pygame.font.Font(os.path.join("space","assets","Font","Sigmar","Sigmar-Regular.ttf"),16)
score=0
texto=font.render('score:',True,(225,225,225))

rectex=texto.get_rect(center=(50,10))


pygame.display.set_caption("space kombat")

r,g,b = 0,0,0
#for tirorec in bullets:
def fire_bullet(bullets):
     
    tirorec= tiro.get_rect(midbottom=navrec.midtop)
    bullets.append(tirorec)


def meteoro_vaic(meteoros):
    if meteorocai=="caindo":
        meteororec=meteoro.get_rect(midtop=(num_rand,0))
        meteoros.append(meteororec)
    



    


loop=True
while loop:
    start = int(round(time.time()*1000))  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             loop = False
             sys.exit()
        
    key = pygame.key.get_pressed()
    if key[pygame.K_s]:
        if navrec.y<=480:
            navrec.y+=6
    if key[pygame.K_w]:
        if navrec.y>=10:
            navrec.y-=6
    if  key[pygame.K_d]:
        navrec.x+=6
    if key[pygame.K_a]:
        navrec.x-=6
    if key[pygame.K_SPACE]:
        if(tiro_estado=='ready'):
            fire_bullet(bullets)

    if navrec.x > 800:
        navrec.x=-80
    if navrec.x < -140:
        navrec.x=800

    num_rand=random.randint(0,800)
    meteoro_vaic(meteoros)

    for tirorec in bullets:
        tirorec.y-=(10)
        tiro_estado=".."
        if tirorec.y < 0:
            tiro_estado="ready"
            bullets.remove(tirorec)
    
    if score <= 5:
        speedmet=2
    if score >= 5:
        speedmet=4  
    if score >= 10:
        speedmet=5
    for meteororec in meteoros:
        #num_caida=random.randint(-10,10)
        meteororec.y+=speedmet
        #meteororec.x-=num_caida
        meteorocai=".."
        if meteororec.y > 600:
            meteoros.remove(meteororec)
            meteorocai="caindo"

    camfre=campoforça.get_rect(center=navrec.center) 
         

    scorerand=font.render(str(score),True,(225,225,225))
    scorerec=scorerand.get_rect(center=(90,11))
    
   

    for i in range(len(meteoros)) :
        for j in range(len(bullets)):
            if bullets[j].colliderect(meteoros[i]):
                score+=1
                meteoros.remove(meteororec)
                bullets.remove(tirorec)
                meteorocai="caindo"
                tiro_estado="ready"
    
    

    if meteororec.colliderect(navrec):
        vidas-=1
        meteoros.remove(meteororec)
        meteorocai="caindo"
    
    if vidas == 0:
        score =0
        vidas=3
    
    
    liferand=font.render(str(vidas),True,(225,225,225))
    liferrec=liferand.get_rect(center=(770,15))
    
    
    relogio.tick(120) 
    tela.blit(fundo,(0,0))
    tela.blit(texto,rectex)
    tela.blit(scorerand,scorerec)
    tela.blit(liferand,liferrec)
    tela.blit(nave, navrec)
    tela.blit(life,liferec)
    for meteororec in meteoros:
        tela.blit(meteoro,meteororec)
    for tirorec in bullets:
        tela.blit(tiro,tirorec)
    #if navrec.y>=10:
       # navrec.y-=1
    ##tela.fill((0,0,0))
    
    tela.blit(campoforça,camfre)
    pygame.display.update()
    end =float(round(time.time()*1000))  
    #print(f"{end-start} ms")
    

    
pygame.quit()
