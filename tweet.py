#!/usr/bin/env python
#coding:utf-8

import os
from twython import Twython

#Twiiter API 
CONSUMER_KEY ='4FA6KqkRGiggbMGJpveVxpGfe'
CONSUMER_SECRET ='7ceW3x3TLZTBe7oTXkkuict2XIUrrzWg8BDvt5iUukUuusyNdm'
ACCESS_KEY ='755238478271643648-VaA4SZdp1jAbxXN50GGoxRIEF3K6OM5'
ACCESS_SECRET ='RIDdtVDhAbc6LDKe88lKIHFORPyRadRkRbfYE3kXiD2hR'
api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

#time stamp
timestamp = 'date +%F_%H:%M:%S'
current_time=os.popen(timestamp).readline().strip()


api.update_status(status='【テスト】現在時刻は'+current_time+'です!')
