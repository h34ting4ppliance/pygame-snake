#!/bin/python3

# SNAKE game written in Python using
# the Pygame library. Probably the
# worst snake ever and also my first
# pygame.
#
# Copyright (C) h34ting4ppliance 2020
#  This project is licensed under the
#  do-whatever-you-want-with-it License

import pygame, time, random

def main():
    pygame.init()
    surface = pygame.display.set_mode((640, 480))
    pygame.display.update()

    r = random.Random()
    ts = time.time()

    score = 0
    shroomx = r.randint(0, 63)
    shroomy = r.randint(0, 47)
    px, py = 31, 23
    pstack = []
    done = False

    direction = "RIGHT"
    while not done:
        if time.time() > ts + 0.15:
            ts = time.time()
            surface.fill((0, 0, 0))

            if len(pstack) > 0:
                for x in range(len(pstack)-1):
                    pstack[x] = pstack[x+1]

                pstack[-1] = (px, py)

            if direction == "RIGHT":
                px += 1
            if direction == "LEFT":
                px -= 1
            if direction == "UP":
                py -= 1
            if direction == "DOWN":
                py += 1

            if px>63: px = 0
            if px<0: px = 63
            if py>47: py = 0
            if py<0: py = 47

            if ((px, py) == (shroomx, shroomy)):
                pstack.append((px, py))
                score += 100
                shroomx, shroomy = r.randint(0, 63), r.randint(0, 47)

            for x in pstack[:-1]:
                if (px, py) == x:
                    done = True
            for x in pstack:
                drawPixel(surface, x, (255, 255, 255))

            drawPixel(surface, (shroomx, shroomy), (255, 0, 255))
            drawPixel(surface, (px, py), (255, 255, 255))
            pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if direction == "DOWN" or direction == "UP":
                    if event.key == pygame.K_RIGHT:
                        direction = "RIGHT"
                    if event.key == pygame.K_LEFT:
                        direction = "LEFT"
                if direction == "RIGHT" or direction == "LEFT":
                    if event.key == pygame.K_UP:
                        direction = "UP"
                    if event.key == pygame.K_DOWN:
                        direction = "DOWN"
                if event.key == pygame.K_ESCAPE:
                    done = True

    print("=== GAME ENDED ===")
    print("Score :", score)
    print("==================")
    
    pygame.quit()
    return

def drawPixel(surface, xy, rgb):
    x, y = xy

    if x>63 or x<0 or y>47 or y<0:
        print("Index out of range.")
        return

    for xx in range(10):
        for yy in range(10):
            surface.set_at((xx+(x*10), yy+(y*10)), rgb)

if __name__=="__main__":
    main()
