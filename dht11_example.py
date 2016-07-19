# -*- coding: utf-8 -*

import RPi.GPIO as GPIO
import dht11
import time
import datetime
import os

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
instance = dht11.DHT11(pin=4)

while True:
    result = instance.read()


    if result.is_valid():
        #discomfort index 
        hukai=0.81*result.temperature+0.01*(result.temperature*(0.99*result.humidity-14.3))+46.3

        #discomfort message
        if hukai<55 and hukai>0:
            message="寒いでしょうね"

        elif hukai>=55 and hukai<60:
            message="肌寒いかもしれません" 

        elif hukai>=60 and hukai<65:
            message="いつもどおりの気分でしょう"

        elif hukai>=65 and hukai<70:
            message="ちょうどいいですね"

        elif hukai>=70 and hukai<75:
            message="暑くはないですね"
                        
        elif hukai>=75 and hukai<80:
            message="ちょっと熱くなってきましたね!"
                             
        elif hukai>=80 and hukai<85:
            message="もはや部屋がサウナですね"

        elif hukai>=85:
            message="松岡修がログインしました"

        #GetTimeStamp
        timestamp = 'date +%F_%H:%M:%S'
        current_time=os.popen(timestamp).readline().strip()

        #print("Last valid input: " + str(datetime.datetime.now()))
        print current_time
        print("気温は%d ℃です" % result.temperature)
        print("湿度は%d %%です" % result.humidity)
        print("不快指数は%d です"% hukai)
        print("%s"% message)


        print("_ _ _ _ _")

    
    

    time.sleep(1)
