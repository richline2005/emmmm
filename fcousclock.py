import time

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        print(f'Time remaining: {seconds//60:02}:{seconds%60:02} ', end='\r')
        time.sleep(1)
        seconds -= 1
    print('Time is up! Focus mode completed.')
