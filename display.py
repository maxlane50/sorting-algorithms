import pygame
import time
from bubble import Bubble
from selection import Selection
from quick import Quick
from insertion import Insertion
from titleArray import TitleArray
pygame.init()

#colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 157, 255)
PURPLE = (42, 45, 118)
WHITE = (255, 255, 255)
GREEN = (0, 225, 0)
DARKGREEN = (0, 80, 0)
GRAY = (250, 252, 187)

#initialize display with given dimensions 
WIDTH = 1000
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#set title of display
pygame.display.set_caption("Sorting Algorithms")

#set clock to help with FPS
clock = pygame.time.Clock()

#import stats font to save time later
statsFont = pygame.font.SysFont('impact', 16)
headerFont = pygame.font.SysFont('impact', 28)

def main():
    while True:
        algoKey = selectionScreen()
        print(algoKey)
        if (algoKey == "B"):
            algo = Bubble()
            algo.sort()
        elif (algoKey == "S"):
            algo = Selection()
            algo.sort()
        elif (algoKey == "Q"):
            algo = Quick()
            algo.sort(0,0)
            time.sleep(5)
        elif (algoKey == "I"):
            algo = Insertion()
            algo.sort()


def updateAlgo(algo):
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            pygame.quit()

    fillScreen(algo)

    presses = pygame.key.get_pressed()
    if (presses[pygame.K_p]):
        pauseAlgo(algo)
        time.sleep(0.2)


def pauseAlgo(algo):
    run = True
    time.sleep(0.5)
    while run:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
    
        presses = pygame.key.get_pressed()
        if (presses[pygame.K_p]):
            run = False
        
        fillScreen(algo)


def fillScreen(algo):
    #set background
    screen.fill(algo.background)

    #update statistics
    comparisonsText = statsFont.render("# of Comparisons: " + str(algo.comparisons), True, WHITE)
    swapsText = statsFont.render("# of Swaps: " + str(algo.swaps), True, WHITE)
    timeCompText = statsFont.render("Time Complexity: " + algo.complexity, True, WHITE)
    headerText = headerFont.render(algo.type, True, WHITE)

    #draw rectangles representing the array
    color = WHITE
    #note: look at making universal update function and outsourcing this for loop
    for i in range(len(algo.nums)):
        color = getRectColor(algo, i)
        pygame.draw.rect(screen, color, (i*10, 500-(algo.nums[i].height*4.9), 10, algo.nums[i].height*4.9))
        pygame.draw.rect(screen, BLACK, (i*10, 500-(algo.nums[i].height*4.9), 10, algo.nums[i].height*4.9), 1)

    #display text
    screen.blit(headerText, (25, 15))
    screen.blit(comparisonsText, (25, 50))
    screen.blit(swapsText, (25, 70))
    screen.blit(timeCompText, (25, 90))

    #make changes to display
    pygame.display.update()


def getRectColor(algo, i):
    color = WHITE
    if (algo.type == "BUBBLE SORT"):
        if (i == algo.curIndex or i == (algo.curIndex + 1)):
            color = WHITE
        else:
            color = algo.nums[i].color
    elif (algo.type == "SELECTION SORT"):
        if (i == algo.curIndex):     
            color = WHITE
        elif(i == algo.minIndex):
            color = BLACK
        else:
            color = algo.nums[i].color
    elif (algo.type == "QUICK SORT"):
        if (i == algo.i or i == algo.j):
            color = WHITE
        elif (i == algo.pivot):
            color = BLACK
        else:
            color = algo.nums[i].color
    elif (algo.type == "INSERTION SORT"):
        if (algo.curIndex == i):
            color = WHITE
        else:
            color = algo.nums[i].color
    return color

def selectionScreen():
    keepGoing = True

    #fonts
    titleFont = pygame.font.SysFont('impact', 72)
    optionsFont = pygame.font.SysFont('impact', 45)

    #title text
    titleText = titleFont.render('ALGORITHM VISUALIZATION', True, GRAY)
    subText = optionsFont.render('(PRESS KEY FOR DESIRED ALGORITHM)', True, GRAY)
    titleText_rect = titleText.get_rect(center = (WIDTH/2, 125))
    subText_rect = subText.get_rect(center = (WIDTH/2, 175))


    #options text
    bubbleText = optionsFont.render('BUBBLE SORT ("B")', True, GRAY)
    selectionText = optionsFont.render('SELECTION SORT ("S")', True, GRAY)
    insertText = optionsFont.render('INSERTION SORT ("I")', True, GRAY)
    quickText = optionsFont.render('QUICK SORT ("Q")', True, GRAY)
    leftBracketText = optionsFont.render("[", True, WHITE)
    rightBracketText = optionsFont.render("]", True, WHITE)
    commaText = optionsFont.render(",", True, WHITE)
    selection = ""

    #create random nums array
    array1 = TitleArray()
    array2 = TitleArray()

    while keepGoing:
        #if user exits window quit display
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()

        #set background
        screen.fill(BLACK)
        
        #set options and title text
        screen.blit(titleText, titleText_rect)
        screen.blit(subText, subText_rect)
        screen.blit(bubbleText, (100, 300))
        screen.blit(selectionText, (550, 300))
        screen.blit(quickText, (100, 350))
        screen.blit(insertText, (550, 350))

        #set array text
        screen.blit(leftBracketText, (10, 20))
        screen.blit(leftBracketText, (10, 420))
        screen.blit(rightBracketText, (985, 20))
        screen.blit(rightBracketText, (985, 420))

        array1.mix()
        array2.mix()

        for i in range(25):
            array1NumText = optionsFont.render(str(array1.array[i].value), True, array1.array[i].color)
            array2NumText = optionsFont.render(str(array2.array[i].value), True, array1.array[i].color)
            screen.blit(array1NumText, ((i+1)*38, 20))
            screen.blit(array2NumText, ((i+1)*38, 420))
            if i != 24:
                screen.blit(commaText, ((i+1)*38 + 25, 20))
                screen.blit(commaText, ((i+1)*38 + 25, 420))

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





#OUTDATED HARDCODED FUNCTIONALITY

#def updateSelection(algo, curIndex, curMin):
#   for event in pygame.event.get():
#
#        if (event.type == pygame.QUIT):
#    
#            pygame.quit()
#    
#    #set background
#    screen.fill(DARKGREEN)
#    #update statistics
#    comparisonsText = statsFont.render("# of Comparisons: " + str(algo.comparisons), True, WHITE)
#    swapsText = statsFont.render("# of Swaps: " + str(algo.swaps), True, WHITE)
#    timeCompText = statsFont.render("Time Complexity: O(n^2)", True, WHITE)
#    headerText = headerFont.render(algo.type, True, WHITE)
#    screen.blit(headerText, (25, 15))
#    screen.blit(comparisonsText, (25, 50))
#    screen.blit(swapsText, (25, 70))
#    screen.blit(timeCompText, (25, 90))
#    #draw rectangles representing the array
#    color = WHITE
#    #note: look at making universal update function and outsourcing this for loop
#   for i in range(len(algo.nums)):
#
#       if (i == curIndex):
#    
#           color = YELLOW
#    
#        elif(i == curMin):
#    
#           color = (68, 85, 235)
#    
#       else:
#    
#            color = WHITE
#    
#       pygame.draw.rect(screen, color, (i*10, 500-(algo.nums[i]*4.9), 10, algo.nums[i]*4.9))
#
#       pygame.draw.rect(screen, BLACK, (i*10, 500-(algo.nums[i]*4.9), 10, algo.nums[i]*4.9), 1)
#
        
#
#    pygame.display.update()
#def updateBubble(bubble, curIndex):
#    for event in pygame.event.get():
#
#        if (event.type == pygame.QUIT):
#    
#            pygame.quit()
#    
#    #set background
#    screen.fill(PURPLE)
#    #update statistics
#    comparisonsText = statsFont.render("# of Comparisons: " + str(bubble.comparisons), True, WHITE)
#    swapsText = statsFont.render("# of Swaps: " + str(bubble.swaps), True, WHITE)
#    timeCompText = statsFont.render("Time Complexity: O(n^2)", True, WHITE)
#    headerText = headerFont.render("BUBBLE SORT", True, WHITE)
#    screen.blit(headerText, (25, 15))
#    screen.blit(comparisonsText, (25, 50))
#    screen.blit(swapsText, (25, 70))
#    screen.blit(timeCompText, (25, 90))
#    #draw rectangles representing the array
#    color = WHITE
#    #note: look at making universal update function and outsourcing this for loop
#    for i in range(len(bubble.nums)):
#       if (i == curIndex or i == (curIndex + 1)):
#           color = YELLOW
#       else:
#           color = WHITE
#       pygame.draw.rect(screen, color, (i*10, 500-(bubble.nums[i]*4.9), 10, bubble.nums[i]*4.9))
#       pygame.draw.rect(screen, BLACK, (i*10, 500-(bubble.nums[i]*4.9), 10, bubble.nums[i]*4.9), 1)
#
#
#    pygame.display.update()
 
main()