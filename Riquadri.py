import pygame
from pygame.locals import*

class RiqScritto():
    def __init__(self,screen,pos,size,testo):
        self.screen=screen
        self.testo=str(testo)

        self.image = pygame.surface.Surface(size)
        self.rect = pygame.Rect((pos[0],pos[1]),[size[0],size[1]])

        self.nero = (0,0,0)
        self.bianco = (255,255,255)
        self.grigio = (200,200,200)
        self.verdeScuro =(74,117,45)

        self.spessore_bordo = 4
    
    def draw(self,tipo=0,punti="",lum=0):
        if tipo==1:
            pygame.draw.rect(self.image,self.verdeScuro,
                            (self.spessore_bordo,self.spessore_bordo,
                            self.rect.width-self.spessore_bordo*2,self.rect.height-self.spessore_bordo*2),
                            self.spessore_bordo)
            self.image.fill(self.verdeScuro)
        elif tipo==2:
            pygame.draw.rect(self.image,self.verdeScuro,
                            (self.spessore_bordo,self.spessore_bordo,
                            self.rect.width-self.spessore_bordo*2,self.rect.height-self.spessore_bordo*2),
                            self.spessore_bordo)
        else:
            pygame.draw.rect(self.image,self.bianco,
                        (self.spessore_bordo,self.spessore_bordo,
                        self.rect.width-self.spessore_bordo*2,self.rect.height-self.spessore_bordo*2),
                        self.spessore_bordo)

        carattere = pygame.font.Font(None,50)
        if lum==1:
            scritta = carattere.render(self.testo+punti,True,self.grigio)
        elif lum==2:
            scritta = carattere.render(self.testo+punti,True,self.verdeScuro)
        else:
            scritta = carattere.render(self.testo+punti,True,self.bianco)
        scrittaRect = scritta.get_rect()
        scrittaRect.left=self.rect.width // 2-scrittaRect.centerx
        scrittaRect.top=self.rect.height // 2-scrittaRect.centery
        self.image.blit(scritta,scrittaRect)

        self.screen.blit(self.image,self.rect)