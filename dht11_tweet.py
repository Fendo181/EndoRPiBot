# -*- coding: utf-8 -*

import RPi.GPIO as GPIO
import dht11
import time
import datetime
import os
from twython import Twython

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
instance = dht11.DHT11(pin=4)



#Twiiter API 
CONSUMER_KEY ='4FA6KqkRGiggbMGJpveVxpGfe'
CONSUMER_SECRET ='7ceW3x3TLZTBe7oTXkkuict2XIUrrzWg8BDvt5iUukUuusyNdm'
ACCESS_KEY ='755238478271643648-VaA4SZdp1jAbxXN50GGoxRIEF3K6OM5'
ACCESS_SECRET ='RIDdtVDhAbc6LDKe88lKIHFORPyRadRkRbfYE3kXiD2hR'
api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)



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
        timestamp ='date +%F_%H:%M'
        current_time=os.popen(timestamp).readline().strip()

#print("Last valid input: " + str(datetime.datetime.now()))

#print("気温は%d ℃です" % result.temperature)
#print("湿度は%d %%です" % result.humidity)
#print("不快指数は%d です"% hukai)
#print("%s"% message)
#print("_ _ _ _ _")

        api.update_status(status = '【気温情報】'+'現在時刻'+current_time
            +'温度:'+str(result.temperature)+'℃です。'+'湿度:'+str(result.humidity)
            +'%です。不快指数は'+str(int(hukai))+'です。'+'(´･ω･`)「'+message+'」'
            )

        break

    time.sleep(1)
