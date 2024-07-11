import pygame
import time

class SongController:
    def __init__(self, songs):
        pygame.mixer.init()
        self.songs = songs
        self.current_song_index = 0
        self.load_song(self.current_song_index)

    def load_song(self, index):
        pygame.mixer.music.load(self.songs[index])

    def play(self):
        pygame.mixer.music.play()

    def pause(self):
        pygame.mixer.music.pause()

    def unpause(self):
        pygame.mixer.music.unpause()

    def next_song(self):
        self.current_song_index = (self.current_song_index + 1) % len(self.songs)
        self.load_song(self.current_song_index)
        self.play()

    def previous_song(self):
        self.current_song_index = (self.current_song_index - 1) % len(self.songs)
        self.load_song(self.current_song_index)
        self.play()
