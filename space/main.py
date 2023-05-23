import pygame
import sys , os,time
import keyboard as kb

pygame.init()
relogio = pygame.time.Clock()
largura,altura=800,600
tela = pygame.display.set_mode((largura,altura))
fundo = pygame.image.load(os.path.join("space","assets","img","espaco.png")).convert_alpha()
nave = pygame.image.load(os.path.join("space","assets","img","ship.png")).convert_alpha()
nave= pygame.transform.scale(nave,(40,40))
fundorec=fundo.get_rect(center=((largura/2,(altura/2))))
tiro= pygame.image.load(os.path.join("space","assets","img","laser.png")).convert_alpha()
#tiro= pygame.transform.scale(tiro,(40,40))
bullets = []
def fire_bullet():
    
    
    tirorec = tiro.get_rect(center=(navrec.midtop))
    bullets.append([tirorec])

    print(bullets)
posy_y=500
posy_x=500

navrec= nave.get_rect(center=(posy_y,posy_x))

print(navrec)

font=pygame.font.Font(os.path.join("space","assets","Font","Sigmar","Sigmar-Regular.ttf"),16)

texto=font.render('Space',True,(65,105,225))

rectex=texto.get_rect(center=(50,10))

pygame.display.set_caption("space kombat")

r,g,b = 0,0,0
#for tirorec in bullets:
    
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
        fire_bullet()
        

          

    relogio.tick(120) 
    tela.blit(fundo,(0,0))
    tela.blit(texto,rectex)
    tela.blit(nave, navrec)
    for tirorec in bullets:
        tela.blit(tiro,tirorec[0])
    #if navrec.y>=10:
       # navrec.y-=1
    ##tela.fill((0,0,0))
    pygame.display.update()
    end =float(round(time.time()*1000))  
    #print(f"{end-start} ms")
    

    
pygame.quit()
