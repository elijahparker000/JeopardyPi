import pygame
pygame.init()
#my_sound = pygame.mixer.Sound('C:/Users/elija/OneDrive/Desktop/PythonScripts/JeopardyProjectRepo/JeopardyPi/Sounds/DailyDoubleSound.mp3')
#my_sound = pygame.mixer.Sound('Sounds/DailyDoubleSound.mp3')
#my_sound.play()
pygame.mixer.music.load("Sounds/DailyDoubleSound.mp3")
pygame.mixer.music.play()

#it has to have time to run or it won't actually make any sound. 
#below code just takes forever so you can hear the clip
for i in range(1000):
  for j in range(100):
    print(str(i+j))
print("done")


