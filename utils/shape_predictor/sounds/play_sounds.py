import pygame
import threading

alarm_running = False
alarm_thread = None

def _alarm_loop():
    pygame.mixer.init()
    sound = pygame.mixer.Sound(r"D:\RANJEET\sap\car_dash\pro1234\utils\shape_predictor\sounds\beep.mp3")
    while alarm_running:
        sound.play()
        pygame.time.wait(int(sound.get_length()*2000))  # Wait for the sound to finish before playing again

def _welcome():
    pygame.mixer.init()
    sound = pygame.mixer.Sound(r"D:\RANJEET\sap\car_dash\pro1234\utils\shape_predictor\sounds\beep.mp3")
    while alarm_running:
        sound.play()
        pygame.time.wait(int(sound.get_length()*2000))  # Wait for the sound to finish before playing again
        
def start_alarm():
    global alarm_running, alarm_thread
    if not alarm_running:
        alarm_running = True
        alarm_thread = threading.Thread(target=_alarm_loop, daemon=True)
        alarm_thread.start()
        print("🚨 Alarm playing...")
        
def welcome_sound():
    global alarm_running, alarm_thread
    if not alarm_running:
        alarm_running = True
        alarm_thread = threading.Thread(target=_welcome, daemon=True)
        alarm_thread.start()
        print("🚨 Alarm playing...")
        
        
def stop_alarm():
    global alarm_running
    if alarm_running:
        alarm_running = False
        pygame.mixer.stop()
        print("✅ Alarm stopped.")

if __name__ == "__main__":
    start_alarm()
    try:
        while True:
            pass  # Keep the script running to allow the alarm to play
    except KeyboardInterrupt:
        stop_alarm()
        print("Exiting...")  