#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import ex1_kwstest as kws
import ex2_getVoice2Text as gv2t
import ex4_getText2VoiceStream as tts
import ex6_queryVoice as dss
import MicrophoneStream as MS
import time
import os
import vlc
import multiprocessing

def Alarm(second, alarm):
    time.sleep(second)
    
    alarm.play()
    print("?")

def find_time(result_mesg):
    res = []
    if '초' in result_mesg :
        location = result_mesg.index('초') - 1    # '초' 앞에 인덱스는 숫자 첫째자리 수
        res.append(result_mesg[location])
        while True:
            print(result_mesg[location])
            if (result_mesg[location-1] is None) or (result_mesg[location-1] not in ['0','1','2','3','4','5','6','7','8','9']) :
                # 그다음 앞에 인덱스가 숫자가 아니거나 아무것도 없을 때
                return res
            else:
                location -= 1
                res.append(result_mesg[location])
    return -1

def main():
    KWSID = ['기가지니', '지니야', '친구야', '자기야']
    alarm = vlc.MediaPlayer("alarm.mp3")
    while 1:
        recog = kws.btn_test(KWSID[0])
        # 기가지니 호출 200
        if recog == 200:
            print("기가지니 호출됨")
            result_mesg = gv2t.getVoice2Text_alarm()
            print(result_mesg)
            if '알람' in result_mesg:
                print("알람을 찾았어요.")
                second = find_time(result_mesg)
                second.reverse()
                second = ''.join(second)

                # p1 = multiprocessing.Process(target=Alarm, args=(int(second), alarm))
                # p1.start() 
                
        # 버튼 누르는 이벤트 100
        elif recog == 100:
            print('알람을 끕니다 스누즈 모드입니다.')
            alarm_off = vlc.MediaPlayer("alarm_off.mp3")
            alarm_off.play()
            os.system('./tt')

if __name__ == '__main__':
    main()

