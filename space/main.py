import pygame
import sys , os,time
import keyboard as kb
import random
from pygame.locals import *

pygame.init()
relogio = pygame.time.Clock()
largura,altura=800,600
tela = pygame.display.set_mode((largura,altura))
fundo = pygame.image.load(os.path.join("space","assets","img","espaco.png")).convert_alpha()
nave = pygame.image.load(os.path.join("space","assets","img","ship.png")).convert_alpha()
nave= pygame.transform.scale(nave,(40,40))
fundorec=fundo.get_rect(center=((largura/2,(altura/2))))
tiro= pygame.image.load(os.path.join("space","assets","img","laser.png")).convert_alpha()
meteoro= pygame.image.load(os.path.join("space","assets","img","meteor.png")).convert_alpha()
#tiro= pygame.transform.scale(tiro,(40,40))
tiro_estado="ready"
meteorocai="caindo"

bullets = []
meteoros=[]



posy_y=500
posy_x=500

navrec= nave.get_rect(center=(posy_y,posy_x))



    


print(navrec)

font=pygame.font.Font(os.path.join("space","assets","Font","Sigmar","Sigmar-Regular.ttf"),16)
score=0
texto=font.render('score:',True,(65,105,225))
scorerand=font.render(str(score),True,(65,105,225))
rectex=texto.get_rect(center=(50,10))
scorerec=scorerand.get_rect(center=(90,11))

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

    
num_caida=random.randint(-10,10)     
loop=True
while loop:
    start = int(round(time.time()*1000))  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             loop = False
             sys.exit()
        
    key = pygame.key.get_pressed()
    if key[pygame.K_s]:
        navrec.y+=3
    if key[pygame.K_w]:
        navrec.y-=3
    if  key[pygame.K_d]:
        navrec.x+=3
    if key[pygame.K_a]:
        navrec.x-=3
    if key[pygame.K_SPACE]:
        if(tiro_estado=='ready'):
            fire_bullet(bullets)
        

    for tirorec in bullets:
        tirorec.y-=(10)
        tiro_estado=".."
        if tirorec.y < 0:
            tiro_estado="ready"
            bullets.remove(tirorec)
    
    num_rand=random.randint(0,800)
    
    for meteororec in meteoros:
        meteororec.y+=5
        #meteororec.x-=num_caida
        meteorocai=".."
        if meteororec.y > 600:
            meteoros.remove(meteororec)
            meteorocai="caindo"

    if tirorec.colliderect(meteororec):
        score+=1
        meteoros.remove(meteororec)
        meteorocai="caindo"  
    

    relogio.tick(120) 
    tela.blit(fundo,(0,0))
    tela.blit(texto,rectex)
    tela.blit(scorerand,scorerec)
    tela.blit(nave, navrec)
    for meteororec in meteoros:
        tela.blit(meteoro,meteororec)
    for tirorec in bullets:
        tela.blit(tiro,tirorec)
    #if navrec.y>=10:
       # navrec.y-=1
    ##tela.fill((0,0,0))
    pygame.display.update()
    end =float(round(time.time()*1000))  
    #print(f"{end-start} ms")
    

    
pygame.quit()
