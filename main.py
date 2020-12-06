from inputs import get_gamepad
from json import load
import subprocess
import inputs
import sys

"""
Buttons: 
BTN_SOUTH
BTN_NORTH
BTN_WEST
BTN_EAST
BTN_SELECT
BTN_START
BTN_THUMBR
BTN_THUMBL
BTN_TR
BTN_TL
ABS_HAT0Y  # Up and Down
ABS_HAT0X  # Left and Right
"""

def main():
    json_content = load(open("input.json", "r"))
    while 1:
        events = get_gamepad()
        for e in events:
            if e.state == 1:
                if e.code not in ["ABS_RY", "ABS_RX", "ABS_Y", "ABS_X", "SYN_REPORT"]:
                    if e.code in json_content:
                        for i in json_content[e.code]:
                            if i.startswith("(@PY)"):
                                eval(i[5:])
                            else:
                                command = subprocess.Popen(i, shell=True, stdout=sys.stdout)
                                command.wait()

if __name__ == "__main__":
    main()