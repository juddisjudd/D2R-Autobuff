import pyautogui
import keyboard
import time
import threading
import pygetwindow as gw
from colorama import init, Fore

init(autoreset=True)

stop_thread = False
t = None  # Declare t here to avoid SyntaxError

def press_keys():
    global stop_thread
    keys = ['f1', 'f1', 'f2', 'f2', 'w', 'f7', 'f7', 'f8', 'f8', 'w'] # Change to your hotkeys (w for weapon swap to cta)
    cooldown_time = 120  # 2 minutes
    while True:
        if stop_thread:
            return
        try:
            win = gw.getActiveWindow()
            if "Diablo II: Resurrected" in win.title:
                print(Fore.GREEN + "Performing key sequence...")
                for key in keys:
                    pyautogui.press(key)
                    time.sleep(0.3)  # Sleep for 0.3 seconds for each key press
                for remaining in range(cooldown_time, 0, -1):
                    if stop_thread:
                        return
                    print(Fore.RED + f"Next key press sequence in {remaining} seconds...", end="\r")
                    time.sleep(1)
            else:
                time.sleep(cooldown_time)
        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(cooldown_time)

def start_pause_thread():
    global stop_thread
    global t
    if t is not None and t.is_alive():
        stop_thread = not stop_thread
        if stop_thread:
            print(Fore.GREEN + "Paused key sequence")
        else:
            print(Fore.GREEN + "Resuming key sequence")
    else:
        stop_thread = False
        t = threading.Thread(target=press_keys)
        t.daemon = True  # Set the thread as a daemon so it will end when the main program ends
        t.start()

def restart_thread():
    global stop_thread
    global t
    if t is not None and t.is_alive():
        stop_thread = True
        t.join()  # Wait for the old thread to finish
    stop_thread = False
    t = threading.Thread(target=press_keys)
    t.daemon = True  # Set the thread as a daemon so it will end when the main program ends
    t.start()

# Set the hotkeys to call the functions
keyboard.add_hotkey('u', start_pause_thread)
keyboard.add_hotkey('r', restart_thread)

# Block forever, to keep the script running. 
keyboard.wait()
