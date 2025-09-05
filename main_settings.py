import pygame
pygame.init()

# Initialize the mixer
pygame.mixer.init()
class Settings:
    trials=2 #1 being the lowest
    show_article=False
    volume_limit=1.0  #0-1
    sound_enable=True
    sound_correct = pygame.mixer.Sound("correct-156911.mp3")
    sound_wrong = pygame.mixer.Sound("error-010-206498.mp3")


