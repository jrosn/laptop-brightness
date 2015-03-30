import sys
import os

# keyboard_brightness_path = '/sys/class/leds/asus::kbd_backlight/brightness'
MONITOR_BRIGHTNESS_PATH = '/sys/class/backlight/intel_backlight/brightness'
MAX_MONITOR_BRIGHTNESS_PATH = '/sys/class/backlight/intel_backlight/max_brightness'


def main():
    if os.getuid() == 0:
        if len(sys.argv) == 2 and sys.argv[1] == 'status':
            print("Current monitor brightness: " + str(get_current_monitor_brightness()))
            print("Max monitor brightness: " + str(get_max_monitor_brightness()))
        elif len(sys.argv) == 3 and sys.argv[1] == 'set':
            set_monitor_brightness(int(sys.argv[2]))
    else:
        print("Need to be as root!")
 

def get_current_monitor_brightness():
    f = open(MONITOR_BRIGHTNESS_PATH, 'r+')
    return int(f.read())


def set_monitor_brightness(new_value):
    f = open(MONITOR_BRIGHTNESS_PATH, 'w')
    f.write(str(new_value))

    
def get_max_monitor_brightness():
    f = open(MAX_MONITOR_BRIGHTNESS_PATH, 'r')
    return int(f.read())
 
    
if __name__ == '__main__':
    main()
