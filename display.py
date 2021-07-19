import pygame
pygame.init()

#colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
LIGHTBLUE = (68, 85, 90)

#initialize display with given dimensions 
WIDTH = 1000
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#set title of display
pygame.display.set_caption("Sorting Algorithms")

#set clock to help with FPS
clock = pygame.time.Clock()

def main():
    algoKey = selectionScreen()
    print(algoKey)

def selectionScreen():
    keepGoing = True

    #fonts
    titleFont = pygame.font.SysFont('impact', 72)
    optionsFont = pygame.font.SysFont('impact', 45)

    #title text
    titleText = titleFont.render('ALGORITHM VISUALIZATION', True, YELLOW)
    subText = optionsFont.render('(PRESS KEY FOR DESIRED ALGORITHM)', True, YELLOW)
    titleText_rect = titleText.get_rect(center = (WIDTH/2, 125))
    subText_rect = subText.get_rect(center = (WIDTH/2, 175))


    #options text
    bubbleText = optionsFont.render('BUBBLE SORT ("B")', True, LIGHTBLUE)
    selectionText = optionsFont.render('SELECTION SORT ("S")', True, LIGHTBLUE)
    insertText = optionsFont.render('INSERTION SORT ("I")', True, LIGHTBLUE)
    quickText = optionsFont.render('QUICK SORT ("Q")', True, LIGHTBLUE)
    selection = ""
    while keepGoing:
        #if user exits window quit display
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                keepGoing = False

        #set background
        screen.fill(BLACK)
        
        #set options and title text
        screen.blit(titleText, titleText_rect)
        screen.blit(subText, subText_rect)
        screen.blit(bubbleText, (100, 300))
        screen.blit(selectionText, (550, 300))
        screen.blit(quickText, (100, 350))
        screen.blit(insertText, (550, 350))

        #check key presses
        presses = pygame.key.get_pressed()
        if (presses[pygame.K_b]):
            selection = "B"
            keepGoing = False
        elif (presses[pygame.K_s]):
            selection = "S"
            keepGoing = False
        elif (presses[pygame.K_i]):
            selection = "I"
            keepGoing = False
        elif (presses[pygame.K_q]):
            selection = "Q"
            keepGoing = False

        #update the screen and set clock
        pygame.display.update()
        clock.tick(60)

    return selection

main()