import cv2
import pygame

from HandGestureController import HandGestureController
from SongController import SongController


def main():
    cap = cv2.VideoCapture(0)
    gesture_controller = HandGestureController()
    songs = ['song1.mp3', 'song2.mp3', 'song3.mp3']
    song_controller = SongController(songs)
    song_controller.play()

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        gesture = gesture_controller.get_gesture(frame)

        if gesture == "pause":
            pygame.mixer.music.pause() if pygame.mixer.music.get_busy() else pygame.mixer.music.unpause()
        elif gesture == "next":
            song_controller.next_song()
        elif gesture == "previous":
            song_controller.previous_song()

        cv2.imshow('Hand Gesture Music Controller', frame)

        if cv2.waitKey(10) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
