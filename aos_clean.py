import platform
import subprocess
import threading
import signal
import sys

# Global variable to store the media player process
current_process = None

ascii_art = """
  ________  ________  ________  ________  ___       ___  ________
 |\   __  \|\   __  \|\   __  \|\   __  \|\  \     |\  \|\   __  \
 \ \  \|\  \ \  \|\  \ \  \|\  \ \  \|\  \ \  \    \ \  \ \  \|\  \
  \ \   ____\ \   __  \ \   __  \ \  \\\  \ \  \  __\ \  \ \   ____\
   \ \  \___|\ \  \ \  \ \  \ \  \ \  \\\  \ \  \|\__\_\  \ \  \___|
    \ \__\    \ \__\ \__\ \__\ \__\ \_______\ \____________\ \__\
     \|__|     \|__|\|__|\|__|\|__|\|_______|\|____________|\|__|
"""

def display_splash_screen():
    os_info = platform.system() + " " + platform.release()
    print("=====================================")
    print(f"Welcome to {ascii_art} CLI ({os_info})")
    print("=====================================")

def play_random_song(folder_path):
    global current_process

    if current_process:
        print("Stopping previous task...")
        current_process.terminate()
        current_process.wait()

    # Adjust the command based on your system and preferred media player
    command = ['cvlc', '--random', folder_path]
    print(f"Executing command: {' '.join(command)}")

    # Use Popen to start the process in the background
    current_process = subprocess.Popen(command)

def play_random_video(folder_path):
    global current_process

    if current_process:
        print("Stopping previous task...")
        current_process.terminate()
        current_process.wait()

    # Adjust the command based on your system and preferred media player
    command = ['vlc', '--random', folder_path]
    print(f"Executing command: {' '.join(command)}")

    # Use Popen to start the process in the background
    current_process = subprocess.Popen(command)

def say_text(text):
    # Use Festival text-to-speech
    command = ['festival', '--tts']
    process = subprocess.Popen(command, stdin=subprocess.PIPE)
    process.communicate(text.encode())

def signal_handler(sig, frame):
    global current_process

    if current_process:
        print("Received signal. Breaking out of the current task...")
        current_process.terminate()
        current_process.wait()

def main():
    display_splash_screen()

    # Register the signal handler for CTRL+C (SIGINT)
    signal.signal(signal.SIGINT, signal_handler)

    while True:
        user_input = input("Please enter a command (type 'exit' to quit): ")

        if user_input == "exit":
            if current_process:
                current_process.terminate()
                current_process.wait()
            sys.exit(0)
        elif user_input == "play random":
            play_random_song("/your/folder/here")
        elif user_input == "play video":
            play_random_video("/your/folder/here"
        elif user_input.startswith("say"):
            text_to_say = user_input[len("robot says"):].strip()
            say_text(text_to_say)
        elif user_input == "break":
            if current_process:
                print("Breaking out of the current task...")
                current_process.terminate()
                current_process.wait()
        else:
            print(f"Unknown command: {user_input}")

if __name__ == "__main__":
    main()

