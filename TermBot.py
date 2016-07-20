#!/usr/bin/env python
#coding:utf-8

#ライブラリをインポートしてくる。
import os
from twython import Twython

#Twitterアカウントの認可情報
CONSUMER_KEY ='key'
CONSUMER_SECRET =key'
ACCESS_KEY ='key'
ACCESS_SECRET ='key'
api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

#Raspbianの制御コマンド（vcgencmd）を実行
cmd = '/opt/vc/bin/vcgencmd measure_temp'
#温度取得(temp=温度) 
line = os.popen(cmd).readline().strip()
#読み込んだ文字列を切り分ける
temp = line.split('=')[1]
#ここで何をしているのかはわからない
#split("")[0]

#時間取得
timestamp = 'date +%F_%H:%M:%S'
current_time=os.popen(timestamp).readline().strip()
#クロック周波数を取得
cmd1 = '/opt/vc/bin/vcgencmd measure_clock arm'
line1 = os.popen(cmd1).readline().strip()
#読み込んだ文字列を切り分ける$
temp1 = line1.split('=')[1]

#電圧#を取得
cmd2 = '/opt/vc/bin/vcgencmd measure_volts core'
line2 = os.popen(cmd2).readline().strip()
#読み込んだ文字列を切り分ける$
temp2 = line2.split('=')[1]

#取得したデータを投稿
api.update_status(status='【CPU情報】'+'現在時刻は'+current_time+'です。CPUの温度は'+temp+'度です！。現在のクロック周波数は'+temp1+'です！''現在の電圧は'+temp2+'ですよ！')
