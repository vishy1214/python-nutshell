import pygame

def play_mp3(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()


if __name__ == "__main__":
    mp3_file_path = "/Users/srishvish/Downloads/entertainer.mp3"  # Replace with the path to your MP3 file
    play_mp3(mp3_file_path)
    input("Press Enter to stop the playback...")
    pygame.mixer.music.stop()
