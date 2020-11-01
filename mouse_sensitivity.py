import subprocess
device_id = "id="
proc = subprocess.Popen(['xinput', '-list'], stdout=subprocess.PIPE)
collected = []
number_of_lines = 4
line_on = 1
while line_on <= number_of_lines:
    line = proc.stdout.readline() 
    if line != '':
        collected.append(line)
        print "text:", line.rstrip()
    line_on += 1
print("----contents collected----")
print(collected[2])
print("----location of device_id----")
print(collected[2].find(device_id))
device_info = collected[2]
print("----device_id----")
print(device_info[54:56])
full_device_id = device_info[54:56]
test_proc = subprocess.Popen(['xinput', 'set-prop', full_device_id, 'libinput Accel Speed', '-1'], stdout=subprocess.PIPE)