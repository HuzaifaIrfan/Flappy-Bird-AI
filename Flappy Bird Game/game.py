import pygame

import time 

import os

import random

from loadimg import loadimg


pygame.font.init()

BG_IMG=loadimg("bg.png")

STAT_FONT=pygame.font.SysFont("comicsans",50)




from Bird import Bird
from Pipe import Pipe

from Base import Base





WIN_HEIGHT=800
WIN_WIDTH=500



def draw_window(win,bird,pipes,base,score):
    win.blit(BG_IMG,(0,0))
    

    base.draw(win)

    for pipe in pipes:
        pipe.draw(win)


    text=STAT_FONT.render("Score: "+str(score),1,(255,255,255))

    win.blit(text,(WIN_WIDTH-10-text.get_width(),10))


    bird.draw(win)


    pygame.display.update()


def main():
    bird=Bird(230,350)

    base=Base(730)

    pipes=[Pipe(700)]

    win= pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
    clock=pygame.time.Clock()

    score=0

    

    run=True
    while(run):
        clock.tick(60)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            
            if event.type==pygame.KEYUP:
                if pygame.K_SPACE:
                    bird.jump()

        rem=[]
        
        add_pipe=False
        for pipe in pipes:
            if pipe.collide(bird):
                pass
            if pipe.x +pipe.PIPE_TOP.get_width()<0:
                rem.append(pipe)

            if not pipe.passed and pipe.x <bird.x:
                pipe.passed=True
                add_pipe=True

            pipe.move()

        if add_pipe:
            score+=1
            pipes.append(Pipe(700))

        for r in rem:
            pipes.remove(r)

        
        if bird.y+bird.img.get_height()>=730:
            pass


        bird.move()
        base.move()
        draw_window(win,bird,pipes,base,score)

    
    pygame.quit()
    quit()

main()