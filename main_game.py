from email.quoprimime import body_check
from imp import C_EXTENSION
from sqlite3 import enable_shared_cache
from tkinter import CENTER
from turtle import update
from unittest.result import failfast
from pygame.math import Vector2

import pygame, sys,random, time

def juegos():
    salir_img = pygame.image.load('assets\\salir.png').convert_alpha()

#---------------------------------------------------------------
#                   C L A S E   D E  F R U T A
#---------------------------------------------------------------
    pygame.mixer.pre_init(44100,-16,2,512)
#Clase de la fruta
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

            if pygame.mouse.get_pressed()[1] == 0:
                self.clicked = False


        #Dibujar boton
            g_screen.blit(self.image, (self.rect.x, self.rect.y))

            return action

    
    back_button = Button(420, 3, salir_img, 1)
        

    def volver():
        corre = True
        while corre:

            g_screen.fill((255, 255, 255))  

            if back_button.draw()== True:
                corre = False
                pygame.quit()
                sys.exit()

            for event in pygame.event.get():
                    #Salir
                if event.type == pygame.QUIT:
                    corre = False
            
        pygame.display.update()

#----------------------------------------------------------------------------------------

    class FRUTA:
        def __init__(self):
            self.aleatorio()
        #Crear posiciones de fruta
        #Posicion en conforme a X la celda
        #Con el random.randint generaremos un intervalo de numeros en ciertos rangos
        #Con 0 que iniciamos al lado de pantalla hasta el numero de celdas que determinemos
        #El hecho de que sea -1 asegura que siempre estemos dentro de la pantalla y no un pixel fuera
            self.x = random.randint(0,num_celda - 1)
        #Posicion en conforme a Y la celda
            self.y = random.randint(0,num_celda -1)
        
        #El vector 2 refiere que es 2D
        #Solo es escribir Vector2 es simplificado con la implementacion de pygame.math
        #Otra manera de escribirlo seria: pygame.math.Vector2()  Pero asi simplificamos codigo
            self.posicion = Vector2(self.x,self.y)

        


        #--------------------------------------------------
        #Investigar los vectores
        #Vectores son similares a las listas pero simplificadas para esta situacion
        #--------------------------------------------------

    #Generacion de LVL UP aletoria
        def aleatorio(self):
        
            self.x = random.randint(0,num_celda - 1)
        #Posicion en conforme a Y la celda
        #self.y = random.randint(0,num_celda - 1)

        #Un posible problema aqui es que el primer valor le vale madre donde sale, idk por que sucede
        #-------------------------------------------------------------------------------------------
            self.y = random.randint(2,19)
        
        #print(self.y)

            self.posicion = Vector2(self.x,self.y)

    #Dibujar la fruta o su celda
        def frutita_d(self):
        #Crear la zona de la fruta y su rectangulo
        #Para la zona de la fruta haremos el rectangulo con ubicacion y medidas
        # X , Y , W , H
        #El int es necesario por problemas de numeros float
            fruit_zone = pygame.Rect(int(self.posicion.x * tam_celda), int(self.posicion.y * tam_celda), tam_celda, num_celda)
        
        #Dibujar la fruta
        #Zona de dibujo, imagen o color, la fruta en ubicacion
        #De hacerlo asi sin imagen del lvlup
        #pygame.draw.rect(g_screen,(120,160,114),fruit_zone)
            self.x = random.randint(0,0)
            self.y = random.randint(0,0)
            self.position = Vector2(self.x,self.y)
            bg = pygame.Rect(int(self.position.x * tam_celda), int(self.position.y * tam_celda), tam_celda, num_celda)
            g_screen.blit(fondo_p,bg)

            g_screen.blit(lvlup,fruit_zone)

#---------------------------------------------------------------
#                C R E A C I O N   D E   S N A K E
#---------------------------------------------------------------
    class SNAKE_C:
        def __init__(self):
        #Creacion del cuerpo
        #Usaramos mismo concepto con Vectores para el cuerpo
        #Con vectores juntos estamos posicionando el cuerpo en conjunto
        #Esta es posicion de inicio btw
            self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
            self.movimiento = Vector2(0,0)
        #Con ello paramos un incremento dejandolo en false
            self.añadir = False

        #---------------------------------------------------------------------------------
        #                        S K I N S    D E L   S N A K E
        #---------------------------------------------------------------------------------
        #Cabeza
            self.head_up = pygame.image.load("assets\\skin\\head_up.png").convert_alpha()
            self.head_down = pygame.image.load("assets\\skin\\head_down.png").convert_alpha()
            self.head_right = pygame.image.load("assets\\skin\\head_right.png").convert_alpha()
            self.head_left = pygame.image.load("assets\\skin\\head_left.png").convert_alpha()

        #Cola
            self.tail_up = pygame.image.load("assets\\skin\\tail_up.png").convert_alpha()
            self.tail_down = pygame.image.load("assets\\skin\\tail_down.png").convert_alpha()
            self.tail_right = pygame.image.load("assets\\skin\\tail_right.png").convert_alpha()
            self.tail_left = pygame.image.load("assets\\skin\\tail_left.png").convert_alpha()

        #Cuerpo
            self.body_up = pygame.image.load("assets\\skin\\body_up.png").convert_alpha()
            self.body_straight = pygame.image.load("assets\\skin\\body_straight.png").convert_alpha()

        #Cuerpo en vuelta
            self.body_turn_right = pygame.image.load("assets\\skin\\body_turn_right.png").convert_alpha()
            self.body_turn_left = pygame.image.load("assets\\skin\\body_turn_left.png").convert_alpha()
            self.body_turn_up = pygame.image.load("assets\\skin\\body_turn_up.png").convert_alpha()
            self.body_turn_straight = pygame.image.load("assets\\skin\\body_turn_straight.png").convert_alpha()

        
    #---------------------------------------------------------------------------------


        """
        Inicio de algoritmo compartido
        -Este es el procesamiento de ubicacion de la skin del snake dependiendo de los vectores de posicionamiento. 
        Esta seccion de codigo fue extraida por el autor:
        Clear code   
        """
        def d_snake(self):

            self.update_hg()

            self.update_tg()

        #Buscamos enumerar los rectangulos del snake con organizador de index 
            for index,bloque_s in enumerate(self.body): 
            #rectangulo
                snake_r = pygame.Rect(int(bloque_s.x * tam_celda), int(bloque_s.y * tam_celda), tam_celda, tam_celda)
        
            #Sentinela de ubicacion de donde se encuentra cada parte del snake
            #Determinando que el index siempre sera 0 sabremos donde iniciaremos la posicion
                if index == 0:
                #Aqui importamos nuestra imagen en la posicion derecha y la necesidad de otro blit
                    g_screen.blit(self.head,snake_r)
            
                elif index == len(self.body) -1:
                    g_screen.blit(self.tail,snake_r)

            #cuerpo graficos
                else:
                    b_next = self.body[index - 1] - bloque_s
                    b_prev = self.body[index + 1] - bloque_s
                    if b_prev.x == b_next.x:
                        g_screen.blit(self.body_up,snake_r)
                
                #Derecho
                    elif b_prev.y == b_next.y:
                        g_screen.blit(self.body_straight,snake_r)

                #Este es para la vuelta izquieda
                    else:
                        if b_prev.x == -1 and b_next.y == -1 or b_prev.y == -1 and b_next.x == -1:
                            g_screen.blit(self.body_turn_left,snake_r)

                        elif b_prev.x == -1 and b_next.y == 1 or b_prev.y == 1 and b_next.x == -1:
                            g_screen.blit(self.body_turn_straight,snake_r)

                        elif b_prev.x == 1 and b_next.y == -1 or b_prev.y == -1 and b_next.x == 1:
                            g_screen.blit(self.body_turn_right,snake_r)

                        elif b_prev.x == 1 and b_next.y == 1 or b_prev.y == 1 and b_next.x == 1:
                            g_screen.blit(self.body_turn_up,snake_r)


        def update_tg(self):
            t_resta_v = self.body[-2] - self.body[-1]
            if t_resta_v == Vector2(1,0): 
                self.tail = self.tail_left
            

            elif t_resta_v == Vector2(-1,0): 
                self.tail = self.tail_right
            

            elif t_resta_v == Vector2(0,1): 
                self.tail = self.tail_up
            

            elif t_resta_v == Vector2(0,-1): 
                self.tail = self.tail_down

        def update_hg(self):
        #Resta de los vectores para idenficar la posicion
            h_resta_v = self.body[1] - self.body[0]
            if h_resta_v == Vector2(1,0): 
                self.head = self.head_left
            

            elif h_resta_v == Vector2(-1,0): 
                self.head = self.head_right
            

            elif h_resta_v == Vector2(0,1): 
                self.head = self.head_up
            

            elif h_resta_v == Vector2(0,-1): 
                self.head = self.head_down
            
        """
        Terminacion de algoritmo compartido
        """      
        

    #-----------------------------------------------------------
    #                       I N C R E M E N TO
    #-----------------------------------------------------------
        def incremento(self):
            self.añadir = True


    #-----------------------------------------------------------
    #               M O V I M I E N T O   B A S E 
    #-----------------------------------------------------------
        def snake_m(self):
        #Copiaremos cortando toda la lista de vectores
        #Es body copy snake
            if self.añadir == True:
                body_c_snake = self.body[:]
                body_c_snake.insert(0,body_c_snake[0] + self.movimiento)

                self.body = body_c_snake[:]
                self.añadir = False
        
            else:

                """
            El concepto del funcionamiento de el movimiento es complicado de entederlo solo escribiendolo.
            Pero una manera de entederlo es que: al momento de tener el "SNAKE" Tomaremos primero el primer vector que va
            en la cabeza, para indicar un movimiento, digamos que a la derecha, para despues en los comandos debajo, tomar
            todos los vectores menos el primero que es la cabeza y luego convertir al anterior a la cabeza, dejandonos con
            que convertimos uno y lo dejamos de la lista e indicando el movimiento.

                """
                body_c_snake = self.body[:-1]
                body_c_snake.insert(0,body_c_snake[0] + self.movimiento)

            #Este es una interpretacion de un return
                self.body = body_c_snake[:]

        #def cr(self):
            #self.comer = pygame.mixer.Sound("assets\\pop.mp3")
            
            #self.comer.play()

        def reset(self):
            self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
            self.movimiento = Vector2(0,0)
#---------------------------------------------------------------
#                        P R I N C I P A L
#---------------------------------------------------------------
    class MAIN:
        def __init__(self):
            self.snake = SNAKE_C()
            self.frutas = FRUTA()

        
        def update(self):
            self.snake.snake_m()
            self.c_choque()
            self.snake_choque()
       

        def draw_elements(self):
            self.frutas.frutita_d()
            #-----------------
            if back_button.draw() == True:
                volver()

            self.contador()
        #self.fondo_bg()

            self.snake.d_snake()
    
    
#-------------------------------------------------------------------------------------------------------
#P O N E R    A T E N C I O N   A Q U I
#-------------------------------------------------------------------------------------------------------
        def fondo_bg(self):
            g_screen.fill(255,255,255)
            self.x = random.randint(0,0)
            self.y = random.randint(0,0)
            self.posicion = Vector2(self.x,self.y)

            bg = pygame.Rect(int(self.posicion.x * tam_celda), int(self.posicion.y * tam_celda), tam_celda, num_celda)
            g_screen.blit(fondo_p,bg)

#--------------------------------------------------------------------------------------------------------
    
        def c_choque(self):
            if self.frutas.posicion == self.snake.body[0]:
           #Para ver si funciona usar el munch
           #print("munch")
                self.frutas.aleatorio()
                self.snake.incremento()
                #self.snake.cr()

        def snake_choque(self):
        #sentinela de choque intencional al snake y perder
        #                cuerpo del snake
        #                          el 0 es la cabeza
        #  Con not decimos si no esta dentro de las zonas en el vector de x
        #Un lose en x osea derecha y izquierda
            if not 0 <= self.snake.body[0].x < num_celda:
                self.game_over()

        
        #Un lose en arriba y abajo

        #Establecemos el borde superior con el 2, para revertir dejar en 0
            if not 2 <= self.snake.body[0].y < num_celda:
                self.game_over()




        #Un for para que por cada rectangulo revisaremos si a partir de la cabeza empieza a colisionar
            for block in self.snake.body[1:]:
                if block == self.snake.body[0]:
                    self.game_over()


#------------------------------------------------------------------------- M O D I F I C A R  P A R A   M E N U
        def game_over(self):
            self.snake.reset()
        

#-------------------------------------------------------------------------

        def contador(self):
            texto_c = str(len(self.snake.body) - 3)
        #Ocupamos el texto, un aa y el color
            contador_g = g_font.render(texto_c,False,(255,255,255))
            c_x = int(tam_celda * num_celda - 300)
            c_y = int(tam_celda * num_celda - 580)
            contador_r = contador_g.get_rect(center = (c_x,c_y))
            g_screen.blit(contador_g,contador_r)
        

       
#---------------------------------------------------------------
#                   I N I C I O   D  E   J U E G O
#---------------------------------------------------------------
#Init del juego
    pygame.init()

#Funcion de el tamaño de celda
    tam_celda = 30

#Nmero de celdas
    num_celda = 20

#Iniciamos creando una ventana de 720 x 480 al igual que nuestro menu en tupla
#Pero para adaptar la pantalla usaremos las medidas de las celdas
    g_screen = pygame.display.set_mode((num_celda * tam_celda ,num_celda * tam_celda))


#Dejamos el icon y caption igual que en el menu
    pygame.display.set_icon(pygame.image.load("assets\\icon.png"))
    pygame.display.set_caption("Snake")

#Icono de el LVL UP y su grafico

    lvlup = pygame.image.load("assets\\lvlup.png").convert_alpha()

    fondo_p = pygame.image.load("assets\\fondo.png").convert_alpha()

#Font del texto
    g_font = pygame.font.Font("assets\\8-BIT WONDER.TTF",35)
#Fruta invocacion
#frutas = FRUTA()


#snake = SNAKE_C()
#Vamos a crear un clock de fps para evitar problemas
    clock = pygame.time.Clock()







#---------------------------------------------------------------------------------
#                                  D I F I C U L T A D 
#---------------------------------------------------------------------------------
#Con los ms podemos cambiar la dificultad
#Si acalanza tiempo haremos dificultad
    Facil = 200
    Normal = 150
    Dificil = 50
    Imposible = 10
    update_pantalla = pygame.USEREVENT
    pygame.time.set_timer(update_pantalla, Normal)



#---------------------------------------------------------------------------------
#                           W H I L E   D E L   J U E G O
#---------------------------------------------------------------------------------
#While del juego, osea para tener el exit

    main_game = MAIN()

    while True:
    #Un loop para cerrar juego
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            #Para estar seguro tambien
                sys.exit()

            if event.type == update_pantalla:
                main_game.update()

        #-------------------------------------------------------------------------
        #                  M O V I M I E N T O   E  N   T E C L A S
        #-------------------------------------------------------------------------
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                #Con esta linea de codigo evitamos que al momento de ir a una direccion, regresar y colisionar con nosotros
                    if main_game.snake.movimiento.y !=1:

                #Con mivimiento hacia arriba usariamos -1 en y
                        main_game.snake.movimiento = Vector2(0,-1)


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if main_game.snake.movimiento.y != -1:
                #Con mivimiento hacia abajo usariamos y en y
                        main_game.snake.movimiento = Vector2(0,1)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if main_game.snake.movimiento.x != -1:
                #Con mivimiento hacia la derecha usariamos 1 en x
                        main_game.snake.movimiento = Vector2(1,0)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if main_game.snake.movimiento.x != 1:
                #Con mivimiento hacia izquierda usariamos -1 en x
                        main_game.snake.movimiento = Vector2(-1,0)
        



    
    #Recuerda hacerlo una tupla
    
    
        main_game.draw_elements()

 
    
     #--------------------------------------------------------------------------------
    #Le estamos que cada vez que demos al while, movera la exposicion del recuadro por mas 1, esto por que se esta actualizando
    #A la derecha es += 1 y izquiera es -= 1
    #game_pos_x -= 1
     #--------------------------------------------------------------------------------
    #Aqui se esta empleando lo descrito
    #test_rect.right += 1
    #g_screen.blit(test_surface,test_rect)

    
    
    #Actualizacion de pantalla de elementos, al igual que la otra en menu
        pygame.display.update()
    #Los fps max del juego
        clock.tick(60)



    #---------------------------------------------------------------------------------
    #                       x    y   w   h
    #test_rect = pygame.Rect(100,200,100,100)
    #                surface - color - rect
    #pygame.draw.rect(g_screen, pygame.Color("Red"), test_rect)



#---------------------------------------------------------------------------------
#                           L O S    E J E M P L O S
#--------------------------------------------------------------------------------
#Definicion de surface de prueba
#test_surface = pygame.Surface((100, 200))

#Esto para llenar de una vez el fondo del surface
#test_surface.fill((0,0,255))

#Con este creamos un rectangulo sobre la superficie creada anteriormente
#test_rect = test_surface.get_rect(center =(360,240))



#Aqui creamos un temporizador de la pantalla para actualizacion de evntos