import os
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(20,GPIO.IN)
GPIO.setup(21.out,initial=GPIO.HIGH)

count_vid = 0
my_vid = "raspivid -o myvid"+str(count_vid)+".h264 "
convertisseur = "MP4Box -fps 30 -add"+str(count_vid)+".h264 myvid"+str(count_vid+)".mp4"
count = 0
flag = false

while True:
    if (GPIO.input(20) && (flag==false)):
        time.sleep(0.05)
        print("Button Pressed "+str(count)
        os.system(my_vid)
        os.system(convertisseur)
    else
        flag = true
