#!/usr/bin/env python
#coding:utf-8

import os
from twython import Twython

#Twiiter API 
CONSUMER_KEY ='key'
CONSUMER_SECRET =key'
ACCESS_KEY ='key'
ACCESS_SECRET ='key'
api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

#time stamp
timestamp = 'date +%F_%H:%M:%S'
current_time=os.popen(timestamp).readline().strip()


api.update_status(status='【テスト】現在時刻は'+current_time+'です!')
