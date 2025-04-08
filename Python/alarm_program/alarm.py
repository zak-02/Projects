from datetime import datetime
import time
import os
from playsound import playsound

alarm = input("What time would you like to set an alarm for: ")
time_alarm = datetime.strptime(alarm, "%I:%M %p").time()

try:
    while True:
        now = datetime.now()
        current_time = now.time().replace(second=0, microsecond=0)

        os.system('cls' if os.name == 'nt' else 'clear')
        print("Current time:", now.strftime("%Y-%m-%d %H:%M:%S"))

        if current_time == time_alarm:
            print("⏰ Alarm time! Playing sound...")
            playsound('alarm_sound.mp3')
            break

        time.sleep(1)

except KeyboardInterrupt:
    print("\nStopped.")
