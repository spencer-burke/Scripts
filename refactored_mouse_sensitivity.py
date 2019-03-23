#!/usr/bin/env python3
import subprocess
import time
time.sleep(60)
number_of_lines, line_on = 4, 1
get_sys_info = subprocess.Popen(['xinput', '-list'], stdout=subprocess.PIPE)
while line_on <= number_of_lines:
    line = get_sys_info.stdout.readline() 
    if line != '' and line_on == 3:
        device_id = line[54:56]
    line_on += 1
set_mouse_sensitivity = subprocess.Popen(['xinput', 'set-prop',device_id, 'libinput Accel Speed', '-1'], stdout=subprocess.PIPE)
