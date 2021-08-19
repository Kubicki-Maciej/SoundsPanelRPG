import pygame as pg
import pathlib
import os


nah = 'E:/SoundsPanel/music/Slither.mp3'



class SoundsPlayer:

    freq = 44100  # audio CD quality
    bitsize = -16  # unsigned 16 bit
    channels = 2  # 1 is mono, 2 is stereo
    buffer = 2048  # number of samples (experiment to get best sound)
    pg.mixer.init(freq, bitsize, channels, buffer)

    def __init__(self):

        self.file_path_playing = None
        self.volume = 0.8

    def load_file(self, file_path):

        try:
            pg.mixer.music.load(file_path)
            print("Music file {} loaded!".format(file_path))
            self.file_path_playing = file_path
        except pg.error:
            print("File {} not found! ({})".format(file_path, pg.get_error()))

    def play_sound(self):
        pg.mixer_music.play()

    def stop_play(self):
        pg.mixer_music.stop()

    def play_fade_out(self):
        pg.mixer_music.fadeout()

    def rewind(self):
        pg.mixer_music.rewind()

    def change_volume(self):
        pg.mixer_music.set_volume(self.volume)


p = SoundsPlayer()


music = "Slither.mp3"





