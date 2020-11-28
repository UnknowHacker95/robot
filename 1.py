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
      #print(name, joy, joy_2)
      rez = joystick.get_button(0)
      if(rez == 1):
          pygame.event.pump()
          rez2 = joystick.get_button(0)
          if(rez2 == 1): r = -r
      if(r == 1):
          if(joy_2 == -3.0517578125e-05): print('...')
          elif(joy_2 < 0): print('Поднять')
          else: print('Опустить')
      else:
          if (joy_2 == -3.0517578125e-05):
              print('Стоим')
          elif (joy_2 < 0):
              print('Вверх')
          else:
              print('Вниз')