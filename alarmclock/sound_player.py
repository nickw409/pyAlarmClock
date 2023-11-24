import platform
import os

if platform.system() == "Linux":
    import pygame
    

class Player:
    def __init__(self):
        if platform.system() == "Linux":
            self.__status = True

            pygame.mixer.pre_init(frequency=44100, size=-16, channels=2)
            pygame.mixer.init()
            sound_file = "solid_snake_is_dummy_thicc.wav"
            script_dir = os.path.dirname(os.path.realpath(__file__))
            project_dir, script_dir = os.path.split(script_dir)
            sound_dir = os.path.join(project_dir, "alarm_sounds",)
            pygame.mixer.music.load(os.path.join(sound_dir, sound_file))
            print("Sound initialized")

        else:
            self.__status = False
            print("pygame not imported, cannot play sound")

    def play(self):
        if self.__status:
            pygame.mixer.music.play()
        
        else:
            print("Sound playing")
        
    def stop(self):
        if self.__status:
            pygame.mixer.music.stop()
        
        else:
            print("Sound stopped")