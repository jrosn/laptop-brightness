import sys
import os


def main():
    if os.getuid() == 0:
        if len(sys.argv) == 2 and sys.argv[1] == 'status':
            print("Current monitor brightness: " + str(get_current_monitor_brightness()))
            print("Max monitor brightness: " + str(get_max_monitor_brightness()))
            print()
            print("Current keyboard brightness: " + str(get_current_keyboard_brightness()))
            print("Max keyboard brightness: " + str(get_max_keyboard_brightness()))
        elif len(sys.argv) == 3 and sys.argv[1] == 'set':
            set_monitor_brightness(int(sys.argv[2]))
        elif len(sys.argv) == 3 and sys.argv[1] == 'kset':
            set_keyboard_brightness(int(sys.argv[2]))
        elif sys.argv[1] == 'help':
            print(get_help())
    else:
        print("Need to be as root!")


#### MONITOR
MONITOR_BRIGHTNESS_PATH = '/sys/class/backlight/intel_backlight/brightness'
MAX_MONITOR_BRIGHTNESS_PATH = '/sys/class/backlight/intel_backlight/max_brightness'


def get_current_monitor_brightness():
    f = open(MONITOR_BRIGHTNESS_PATH, 'r')
    return int(f.read())


def set_monitor_brightness(new_value):
    f = open(MONITOR_BRIGHTNESS_PATH, 'w')
    f.write(str(new_value))

    
def get_max_monitor_brightness():
    f = open(MAX_MONITOR_BRIGHTNESS_PATH, 'r')
    return int(f.read())


#### KEYBOARD
KEYBOARD_BRIGHTNESS_PATH = '/sys/class/leds/asus::kbd_backlight/brightness'
MAX_KEYBOARD_BRIGHTNESS_PATH = '/sys/class/leds/asus::kbd_backlight/max_brightness' 


def get_current_keyboard_brightness():
    f = open(KEYBOARD_BRIGHTNESS_PATH, 'r')
    return int(f.read())


def set_keyboard_brightness(new_value):
    f = open(KEYBOARD_BRIGHTNESS_PATH, 'w')
    f.write(str(new_value))


def get_max_keyboard_brightness():
    f = open(MAX_KEYBOARD_BRIGHTNESS_PATH, 'r')
    return int(f.read())


### COMMON
def get_help():
    return "Keyboard and monitor brightness controller.\nAuthor: Roman Sosnovsky\n\n" \
           "usage: brightness <command> [<args>]\n\n" \
           "brightness commands:\n" \
           "   status     get current status\n" \
           "   set        set monitor brightness level\n" \
           "   kset       set keyboard brightness level\n" \
           "   help       get detailed help"


if __name__ == '__main__':
    main()
