from pickle import FALSE
from tkinter import Menu
from turtle import width
import pygame
#from ejem import juego
from main_game import juegos

from sys import exit


pygame.mixer.pre_init(44100,16,2,4096)

#Es necesario python init en cualquier inicio de python para iniciar el juego
pygame.init()

#---------------------------------------------------------------------------------
#                       B A C K G R O U N D     M U S I C
#---------------------------------------------------------------------------------
pygame.mixer.music.load("assets\\spacedust.mp3")
#Con intervalo de 0 a 1 el valor de volumen
pygame.mixer.music.set_volume(0.3)
#Con -1 damos que sea un loop
pygame.mixer.music.play(-1)
#---------------------------------------------------------------------------------
#                   T A M A Ñ O    D E   P A N T A L L A
#---------------------------------------------------------------------------------
#Estableciendo el tamñano de la screen
SCREEN_WIDTH =600 #600  
SCREEN_HEIGHT =600 #600  

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake")

pygame.display.set_icon(pygame.image.load("assets\\icon.png"))

#---------------------------------------------------------------------------------
#Aqui invocamos una funcion dando a variable para establecer un frame rate
clock = pygame.time.Clock()

#---------------------------------------------------------------------------------
#                        C A R G A R   I M A G E N E S
#---------------------------------------------------------------------------------
#Cargar las imagenes
words_img = pygame.image.load('assets\\words.png').convert_alpha()

snake_img = pygame.image.load('assets\\snake.png').convert_alpha()

start_img = pygame.image.load('assets\\start.png').convert_alpha()

options_img = pygame.image.load('assets\\options.png').convert_alpha()

credits_img = pygame.image.load('assets\\credits.png').convert_alpha()

exit_img = pygame.image.load('assets\\exit.png').convert_alpha()

ic_img = pygame.image.load('assets\\ic.png').convert_alpha()

back_img = pygame.image.load('assets\\back.png').convert_alpha()


#---------------------------------------------------------------------------------
#                                     B O T O N
#---------------------------------------------------------------------------------
#Crear una clase para los botones
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        #Transformacion de la escala
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))

        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

        self.clicked = False

    def draw(self):
        action = False
        #Ubicador de mouse
        pos = pygame.mouse.get_pos()
        #print("pos") para saber si estamos en la posicion

        #Como saber si el mouse esta sobre un boton
        if self.rect.collidepoint(pos):
            #print("sobre") para saber si estamos sobre los botones
            #El 0 es click izquierdo, 1 el de la ruedita y 2 el derecho
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                #print("click") para saber si estamos dando click donde se debe
                #Un problema que da es que lo registra mas de una vez el click asi que tengemos tener un trigger con valor false
                self.clicked = True
                action = True
                
#---------------------------------------------------------------------------------
#                                   R E V I S A R
#---------------------------------------------------------------------------------
        #Revisar si se acciona el juego ponerlo en en 1 el primer valor
        if pygame.mouse.get_pressed()[1] == 0:
            self.clicked = False


        #Dibujar boton
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action


#---------------------------------------------------------------------------------
#               D E F I N I C I O N    D E   B O T O N E S
#---------------------------------------------------------------------------------
#Crear el boton  # La escala de 1 es su estado normal
#Words es titulo
#words_button = Button(90, -40, words_img, 1)

#Snake es el fondo
snake_button = Button(0, 0, snake_img, 1)

#start_button = Button(280,180, start_img, 1) En caso de tener opciones
start_button = Button(220, 240, start_img, 1)

#options_button = Button(280, 240, options_img, 1)

credits_button = Button(220, 300, credits_img, 1)

exit_button = Button(220, 360, exit_img, 1)

ic_button = Button(70,50, ic_img,1)

back_button = Button(10, 550, back_img, 1)

#---------------------------------------------------------------------------------
#                           M E N U  P R I N C I P A L
#---------------------------------------------------------------------------------
def main_menu():
    run = True
    while run:
        
        #Color del fondo
        #screen.fill((234, 219, 179))
        screen.fill((255, 255, 255))

        #Dibujar en el canvas los botones

        #Words es el titulo
        #if words_button.draw()== True:
            #print()

        #Snake es el fondo
        snake_button.draw()
            

        #Start es iniciar
        if start_button.draw() == True:
            juegos()
    
        #Usar en caso de tener opciones
        #if options_button.draw() == True:
            #print("opciones")

        if credits_button.draw() == True:
            creditos_menu()

        if exit_button.draw() == True:
            #Aqui para salir solo convertimos la variable que corre el juego a un false
            run = False
            

    
        #Mantiene evento
        for event in pygame.event.get():
            #Salir
            if event.type == pygame.QUIT:
                run = False
    
        pygame.display.update()


#---------------------------------------------------------------------------------
#                       M E N U   D E  C R E D I T O S
#---------------------------------------------------------------------------------
def creditos_menu():
    corre = True
    while corre:

        screen.fill((255, 255, 255))  

        snake_button.draw()

        ic_button.draw()

        if back_button.draw()== True:
            corre = False
            main_menu()

        for event in pygame.event.get():
            #Salir
            if event.type == pygame.QUIT:
                corre = False
            
        pygame.display.update()

#---------------------------------------------------------------------------------
#                                E S T O   C O R R E   E L  J U E G O
#---------------------------------------------------------------------------------
principal_menu = main_menu()

while principal_menu is True:
    main_menu()


pygame.quit()
#---------------------------------------------------------------------------------
#                                 C R E D I T O S
#---------------------------------------------------------------------------------
"""
Cabe destacar que en el desarrollo del videojuego y del menu, tomamos en consideracion las referencias de diversos
autores, es por ello que aqui se presentaran las referencias correspondientes a ellos. | Todos los datos apoyados en las
referencias son libres de copyright |

-Pygame, pygame documentation
https://www.pygame.org/docs/



-ChristianD37
Basic game start
Repository 
    Menu systems 
    Tile Collisions
    Game states
    Framerate Independence
https://github.com/ChristianD37



-Chris -- Clear Coder
UltimatePygameIntro
Collisions
GameDevIntro
PygameTimer

https://www.patreon.com/clearcode
https://github.com/clear-code-projects


-Baraltech
Pygame-Setup
Menu-System-Pygame

https://github.com/baraltech



-Google Snake Game
Las imagenes de la skin del "Snake" fueron conseguidas por del mismo juego

https://g.co/kgs/dpXpcR



-ccMixter
Cancion de background space dust, por: mwic
Conseguida con licencia sin distribucion pero con referencias.

http://dig.ccmixter.org/files/airtone/64741



-dafont.com
Origen de descarga de la 8-BIT-FONT

https://www.dafont.com/8bit-wonder.font



-Imagen de lvl up (el aguacate):

Creditos al aguacate; fue hecho por nosotros pero nos basamos en imagenes de internet




-Para imagenes generales fueron creadas por nosotros.




--- Creditos de investigacion para transformacion del programa a exe ---

-Python Simplified

https://www.youtube.com/watch?v=Y0HN9tdLuJo

"""