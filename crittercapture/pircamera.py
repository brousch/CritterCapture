#!/usr/bin/python2.7
import RPi.GPIO as GPIO
import time
import picamera
import datetime


def get_file_name():
    return datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S.h264")

sensorPin = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensorPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

prevState = False
currState = False

cam = picamera.PiCamera()

while True:
    time.sleep(.1)
    prevState = currState
    currState = GPIO.input(sensorPin)
    if currState != prevState:
        print "GPIO pin {0} is {1}".format(sensorPin, "HIGH" if currState else "LOW")
        if currState:
            fileName = get_file_name()
            cam.start_preview()
            cam.start_recording(fileName)
        else:
            cam.stop_preview()
            cam.stop_recording()
