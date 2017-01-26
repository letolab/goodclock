import subprocess
import settings


def on():
    subprocess.call("sudo /home/pi/hub-ctrl -h 0 -P 2 -p 1", shell=True)

def off():
    subprocess.call("sudo /home/pi/hub-ctrl -h 0 -P 2 -p 0", shell=True)
