import pygame
import sys
pygame.init()
from pygame.locals import *
pygame.joystick.init()
r = -1
while True:
    pygame.event.pump()
    joystick_count = pygame.joystick.get_count()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    name = joystick.get_name()
    axes = joystick.get_numaxes()
    hats = joystick.get_numhats()
    button = joystick.get_numbuttons()
    joy = joystick.get_axis(0)
    joy_2 = joystick.get_axis(1)
    joy_3 = joystick.get_axis(2)
    joy_4 = joystick.get_axis(3)
    #print(name, joy_3, joy_4)
    jamk = joystick.get_button(0)
    rez = joystick.get_button(3)
    pygame.event.pump()
    rez2 = joystick.get_button(3)
    jamk2 = joystick.get_button(0)

    if(rez == 1 and rez2 == 1): r = -r
    if(jamk == 1 and jamk2 == 1): print('СЖИМАЕМ КЛЕШНЮ')
    #r = -1 -- это ручной режим, r = 1  -- автономный
    if(r == -1):
        #клешня    (ось вверх-вниз)
        if(joy_3 == -3.0517578125e-05): print('...')
        elif(joy_3 < 0): print('Поднять')
        else: print('Опустить')

        #робот вверх-вниз + влево-вправо
        if (joy_2 == -3.0517578125e-05):
            print('Стоим')
        elif (joy_2 < 0):
            print('Вверх')
        else:
            print('Вниз')
        if (joy < 0):
            print('Влево)')
        elif (joy == 0):
            print('Прямо')
        else:
            print('Вправо!')
    else: print('AUTO!!!!!!!!!!!!!!')