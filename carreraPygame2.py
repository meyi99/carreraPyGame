'''
Created on 6 abr. 2019

@author: meyi
'''
import pygame, sys

class Game():
    '''
    classdocs
    '''
    runners = []
    __starLine = 20
    __finishLine = 1004


    def __init__(self):
        '''
        Constructor
        '''
        self.__screen = pygame.display.set_mode((1024, 1024))
        self.__background = pygame.image.load("/home/meyi/Imágenes/Wallpapers/carretera1.jpg")
        pygame.display.set_caption("Carrera")
    
    def competir(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True    
            
            self.__screen.blit(self.__background, (0, 0))
            pygame.display.flip()
            
        pygame.quit()
        sys.exit()
        
if __name__ == "__main__":
    game = Game()
    pygame.init()
    game.competir()






    