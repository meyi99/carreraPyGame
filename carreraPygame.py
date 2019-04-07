'''
Created on 6 abr. 2019

@author: meyi
'''
import pygame, sys, random

class Runner():
    '''
    Atributos
    '''
    shape = ["carRed", "camioneta", "camionetaBlue", "truck"]
    
    def __init__(self, x=0, y=0):
        '''
        Construcor
        '''
        ixShape = random.randint(0, 3)
        
        self.shape = pygame.image.load("/home/meyi/Imágenes/Wallpapers/{}.png".format(self.shape[ixShape]))
        self.position = [x, y]
        self.name = ""
        
    def avanzar(self):
        self.position[0] += random.randint(1, 3)

class Game():
    '''
    Atributos
    '''
    runners = []
    posY = (200, 336, 490, 600)
    names = ("Player 1", "Player 2", "Player 3", "Player 4")
    __starLine = -5
    __finishLine = 620


    def __init__(self):
        '''
        Constructor
        '''
        self.__screen = pygame.display.set_mode((640, 840))
        self.__background = pygame.image.load("/home/meyi/Imágenes/Wallpapers/background-1.png")
        pygame.display.set_caption("Carrera")
        
        for i in range(4):
            player = Runner(self.__starLine, self.posY[i])
            player.names = self.names[i]
            self.runners.append(player)

    
    def competir(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True    
            
            for runner in self.runners:
                runner.avanzar()
                if runner.position[0] >= self.__finishLine:                        
                    print("{} ha ganado".format(runner.names))
                    gameOver = True
            
            self.__screen.blit(self.__background, (0, 0))
            
            for i in self.runners:
                self.__screen.blit(i.shape, i.position)
            pygame.display.flip()
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:    
                    pygame.quit()
                    sys.exit()
        
if __name__ == "__main__":
    game = Game()
    pygame.init()
    game.competir()






    