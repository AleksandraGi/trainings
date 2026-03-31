# source: https://www.youtube.com/watch?v=no5dz0GOWy8&list=PLzMcBGfZo4-kBvY2DaxdSvoN_jGpzbw5V&index=2
# sound source: https://www.fesliyanstudios.com/royalty-free-sound-effects-download/alarm-203

import time
from playsound3 import playsound
# playsound("alarm_clock\\alarm.mp3")

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"         # clears entire terminal

def alarm(seconds):             # how long the app will play alarm sound
    time_elapsed = 0

    print(CLEAR)

    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60      # 125 // 60 = 2
        seconds_left = time_left % 60       # 125 % 60 = 5

        print(F"{CLEAR_AND_RETURN}ALARM WILL SOUND IN: {minutes_left:02d}:{seconds_left:02d}")     # :02d formatting   9 -> 09

    playsound("alarm_clock\\alarm.mp3")

minutes = 0             # how many minutes to play the alarm sound
seconds = 5             # how many seconds to play the alarm sound
total_seconds = minutes * 60 + seconds

alarm(total_seconds)
