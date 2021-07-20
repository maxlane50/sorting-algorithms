import pygame
from bubble import Bubble
pygame.init()

#colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
LIGHTBLUE = (68, 85, 90)
PURPLE = (42, 45, 118)
WHITE = (255, 255, 255)
GREEN = (0, 225, 0)

#initialize display with given dimensions 
WIDTH = 1000
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#set title of display
pygame.display.set_caption("Sorting Algorithms")

#set clock to help with FPS
clock = pygame.time.Clock()

#import stats font to save time later
statsFont = pygame.font.SysFont('impact', 12)

def main():
    run = True
    while run:
        algoKey = selectionScreen()
        print(algoKey)
        if (algoKey == "B"):
            algo = Bubble()
            algo.sort()
        elif (algoKey == "S"):
            selection()
        elif (algoKey == "Q"):
            quick()
        elif (algoKey == "I"):
            insertion()
        run = endScreen()

def updateBubble(bubble, curIndex):
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            pygame.quit()

    #set background
    screen.fill(PURPLE)

    #update statistics
    comparisonsText = statsFont.render("# of Comparisons: " + str(bubble.comparisons), True, WHITE)
    swapsText = statsFont.render("# of Swaps: " + str(bubble.swaps), True, WHITE)
    screen.blit(comparisonsText, (50, 25))
    screen.blit(swapsText, (250, 25))

    #draw rectangles representing the array
    color = WHITE
    #note: look at making universal update function and outsourcing this for loop
    for i in range(len(bubble.nums)):
        if (i == curIndex or i == (curIndex + 1)):
            color = GREEN
        else:
            color = WHITE
        pygame.draw.rect(screen, color, (i*10, 500-(bubble.nums[i]*4.9), 10, bubble.nums[i]*4.9))

    pygame.display.update()

def endScreen():
    return True


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