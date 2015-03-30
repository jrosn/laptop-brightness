import sys

# keyboard_brightness_path = '/sys/class/leds/asus::kbd_backlight/brightness'
MONITOR_BRIGHTNESS_PATH = '/sys/class/backlight/intel_backlight/brightness'

def main():
    if len(sys.argv) == 2 and sys.argv[1] == 'status':
        print(get_current_monitor_brightness())
    elif len(sys.argv) == 3 and sys.argv[1] == 'set':
        set_monitor_brightness(int(sys.argv[2]))


def get_current_monitor_brightness():
    f = open(MONITOR_BRIGHTNESS_PATH, 'r+')
    return int(f.read())


def set_monitor_brightness(new_value):
    f = open(MONITOR_BRIGHTNESS_PATH, 'w')
    f.write(str(new_value))


if __name__ == '__main__':
    main()
