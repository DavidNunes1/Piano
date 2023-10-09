import  keyboard
import pygame
import time

# Definir cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Inicializar o Pygame
pygame.init()

# Definir as dimensões da janela
size = (800, 300)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Piano")


done = False


clock = pygame.time.Clock()

Notas = ["dob","re", "mi","fa", "sol", "la","si", "doa","dobs", "res","fas", "sols", "las", "doas"]
cor = WHITE

while not done:
    xmN = 0
    yN = 0
    lN = 100
    aN = 300
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


    
    for i in range(len(Notas)):
        if Notas[i] == "dob":
            xmN = 0
            cor=WHITE
            aN = 300
            lN = 100
        if Notas[i] == "re":
            xmN = 100
            cor=WHITE
            aN = 300
            lN = 100
        if Notas[i] == "mi":
            xmN = 200
            cor=WHITE
            aN = 300
            lN = 100
        if Notas[i] == "fa":
            xmN = 300
            cor=WHITE
            aN = 300
            lN = 100
        if Notas[i] == "sol":
            xmN = 400
            cor=WHITE
            aN = 300
            lN = 100
        if Notas[i] == "la":
            xmN = 500
            cor=WHITE
            aN = 300
            lN = 100
        if Notas[i] == "si":
            xmN = 600
            cor=WHITE
            aN = 300
            lN = 100
        if Notas[i] == "doa":
            xmN = 700
            cor=WHITE
            aN = 300
            lN = 100
        if Notas[i] == "dobs":
            xmN = 75
            cor=BLACK
            aN = 200
            lN = 50
        if Notas[i] == "res":
            xmN = 175 
            cor=BLACK
            aN = 200
            lN = 50
        if Notas[i] == "fas":
            xmN = 375
            cor=BLACK
            aN = 200
            lN = 50
        if Notas[i] == "sols":
            xmN = 475
            cor=BLACK
            aN = 200
            lN = 50
        if Notas[i] == "las":
            xmN = 575
            cor=BLACK
            aN = 200
            lN = 50
        if Notas[i] == "doas":
            xmN = 775
            cor=BLACK
            aN = 200
            lN = 50
        
         
        pygame.draw.rect(screen, cor, [xmN, yN, lN, aN])
        print(xmN, yN, lN,aN)
        if Notas[i] == "dob" or Notas[i] == "re" or Notas[i] == "mi" or Notas[i] == "fa" or Notas[i] == "sol" or Notas[i] == "la" or Notas[i] == "si" or Notas[i] == "doa":
            pygame.draw.rect(screen, BLACK, [xmN, yN, 2, 300])

    #pygame.draw.rect(screen, WHITE, [0, 0, 100, 300])
    #pygame.draw.rect(screen, WHITE, [100, 0, 100, 300])
    #pygame.draw.rect(screen, WHITE, [200, 0, 100, 300])
    #pygame.draw.rect(screen, WHITE, [300, 0, 100, 300])
    #pygame.draw.rect(screen, WHITE, [400, 0, 100, 300])
    #pygame.draw.rect(screen, WHITE, [500, 0, 100, 300])
    #pygame.draw.rect(screen, WHITE, [600, 0, 100, 300])
    #pygame.draw.rect(screen, WHITE, [700, 0, 100, 300])

    #pygame.draw.rect(screen, BLACK, [75, 0, 50, 200])
    #pygame.draw.rect(screen, BLACK, [175, 0, 50, 200])
    ##pygame.draw.rect(screen, BLACK, [275, 0, 50, 200])
    #pygame.draw.rect(screen, BLACK, [375, 0, 50, 200])
    #pygame.draw.rect(screen, BLACK, [475, 0, 50, 200])
    #pygame.draw.rect(screen, BLACK, [575, 0, 50, 200])
    ##pygame.draw.rect(screen, BLACK, [675, 0, 50, 200])
    #pygame.draw.rect(screen, BLACK, [775, 0, 50, 200])

    #pygame.draw.rect(screen, BLACK, [0, 0, 2, 300])
    #pygame.draw.rect(screen, BLACK, [100, 0, 2, 300])
    #pygame.draw.rect(screen, BLACK, [200, 0, 2, 300])
    #pygame.draw.rect(screen, BLACK, [300, 0, 2, 300])
    #pygame.draw.rect(screen, BLACK, [400, 0, 2, 300])
    #pygame.draw.rect(screen, BLACK, [500, 0, 2, 300])
    #pygame.draw.rect(screen, BLACK, [600, 0, 2, 300])
    #pygame.draw.rect(screen, BLACK, [700, 0, 2, 300])
    #pygame.draw.rect(screen, BLACK, [800, 0, 2, 300])
        
        if keyboard.is_pressed('a'):
            if Notas[i] == 'dob':
                pygame.draw.rect(screen, RED, [xmN, yN, lN, aN])
        if keyboard.is_pressed('s'):
            if Notas[i] == 're':
                pygame.draw.rect(screen, RED, [xmN, yN, lN, aN])
        if keyboard.is_pressed('d'):
            if Notas[i] == 'mi':
                pygame.draw.rect(screen, RED, [xmN, yN, lN, aN])
        if keyboard.is_pressed('f'):
            if Notas[i] == 'fa':
                pygame.draw.rect(screen, RED, [xmN, yN, lN, aN])
        if keyboard.is_pressed('g'):
            if Notas[i] == 'sol':
                pygame.draw.rect(screen, RED, [xmN, yN, lN, aN])
        if keyboard.is_pressed('h'):
            if Notas[i] == 'la':
                pygame.draw.rect(screen, RED, [xmN, yN, lN, aN])
        if keyboard.is_pressed('j'):
            if Notas[i] == 'si':
                pygame.draw.rect(screen, RED, [xmN, yN, lN, aN])
        if keyboard.is_pressed('k'):
            if Notas[i] == 'doa':
                pygame.draw.rect(screen, RED, [xmN, yN, lN, aN])
        if keyboard.is_pressed('w'):
            if Notas[i] == 'dobs':
                pygame.draw.rect(screen, RED, [xmN, yN, lN, aN])
        if keyboard.is_pressed('e'):
            if Notas[i] == 'res':
                pygame.draw.rect(screen, RED, [xmN, yN, lN, aN])           
        if keyboard.is_pressed('t'):
            if Notas[i] == 'fas':
                pygame.draw.rect(screen, RED, [xmN, yN, lN, aN])
        if keyboard.is_pressed('y'):
            if Notas[i] == 'sols':
                pygame.draw.rect(screen, RED, [xmN, yN, lN, aN])
        if keyboard.is_pressed('u'):
            if Notas[i] == 'las':
                pygame.draw.rect(screen, RED, [xmN, yN, lN, aN])
        if keyboard.is_pressed('o'):
            if Notas[i] == 'doas':
                pygame.draw.rect(screen, RED, [xmN, yN, lN, aN])


    pygame.display.update()

    

pygame.quit()