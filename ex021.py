import pygame

pygame.mixer.init()
pygame.mixer.music.load('ex021 (2).mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    continue