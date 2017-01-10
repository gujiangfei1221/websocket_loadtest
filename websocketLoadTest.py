#!/usr/bin/python
# -*- coding: UTF-8 -*-
import threading
import time
import websocket
import datetime

#单个线程执行的次数
count = 1
#线程数
thead_count = 3
#思考时间
sleeptime = 0
#运行模式，1为按次数，2为按时间
mode = 2
#运行的时间,单位为秒
total_time = 60
m_list = []
tsk = []
m_mode2_count = []

class myThread (threading.Thread):   #继承父类threading.Thread
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        if(mode == 1):
            # print("Starting " + self.name + ",当前时间：" +str(datetime.datetime.now()))
            starttime = datetime.datetime.now()
            websocketLogic(self, count)
            endtime = datetime.datetime.now()
            # print("Exiting " + self.name + ",当前时间：" +str(datetime.datetime.now()))
            spenttime = endtime - starttime
            print(self.name + "的TPS：" + str(float(count) / float(spenttime.total_seconds())) + ",总共循环：" + str(count) + "次，花费时间：" + str(spenttime))
            m_list.append(float(spenttime.total_seconds()))
        elif(mode == 2):
            # print("Starting " + self.name + ",当前时间：" +str(datetime.datetime.now()))
            starttime = datetime.datetime.now()
            m_count = websocketLogic2(self, total_time)
            endtime = datetime.datetime.now()
            # print("Exiting " + self.name + ",当前时间：" +str(datetime.datetime.now()))
            spenttime = endtime - starttime
            print(self.name + "的TPS：" + str(float(m_count) / float(spenttime.total_seconds()))+",总共运行次数："+ str(m_count) + ",总共花费时间：" + str(spenttime))
            m_list.append(float(spenttime.total_seconds()))
            m_mode2_count.append(m_count)
        else:
            print("请确认运行模式！")
            return

def websocketLogic(self,counter):
    i = 0
    self.ws = websocket.WebSocket()
    try:
        self.ws.connect("ws://192.168.201.30:8090/EpointFrame-9.1.2/websocket/eXun?X-Atmosphere-tracking-id=0&X-Atmosphere-Framework=2.2.12-javascript&X-Atmosphere-Transport=websocket&Content-Type=application/json&X-atmo-protocol=true&uid=45f0c5f9-cad2-49e6-887d-b38dfcbc23de&uname=%E7%B3%BB%E7%BB%9F%E7%AE%A1%E7%90%86%E5%91%98%20")
        while i < counter:
            self.ws.send('{"type":"message","sessionid":"5e874c2f-4206-43ee-934c-2b320d69386e","from_uid":"45f0c5f9-cad2-49e6-887d-b38dfcbc23de","from_name":"系统管理员 ","content":"11111"}')
            time.sleep(sleeptime)
            i = i + 1
        self.ws.close()
    except Exception as e:
        print("请检查系统是否可以访问，该线程中断！")
        print("异常为："+str(e))
        self.ws.close()
        return

def websocketLogic2(self,total_time):
    i = 0
    self.ws = websocket.WebSocket()
    try:
        m_start = datetime.datetime.now()
        m_dleta = 0
        self.ws.connect("ws://192.168.203.223:7272")
        self.ws.send('{"type":"login","client_name":"111","room_id":"1"}')
        self.ws.recv()
        while m_dleta < total_time:
            i = i + 1
            self.ws.send('{"type":"say","to_client_id":"all","to_client_name":"所有人","content":"1111"}')
            time.sleep(sleeptime)
            m_end = datetime.datetime.now()
            m_dleta = (m_end - m_start).total_seconds()
        self.ws.close()
        return i
    except Exception as e:
        print("请检查系统是否可以访问，该线程中断！")
        print("异常为："+str(e))
        self.ws.close()
        return

if __name__ == '__main__':
    m_max = 0.0
    print("=======================测试开始，模式："+str(mode)+"=======================")
    for i in range(0,thead_count):
        thread = myThread(i,"线程："+ str(i),i)
        thread.start()
        tsk.append(thread)

    for tt in tsk:
        tt.join()

    print("Exiting Main Thread")

    for i in m_list:
        m_max = max(m_list)
    print("==============================测试结果=====================================")
    if(mode == 1):
        print("合计线程数：" + str(thead_count) + "，合计运行次数：" + str(count * thead_count) + "，合计运行时间：" + str(m_max) + "秒，总TPS为：" + str(float(count * thead_count) / float(m_max)))
    elif(mode == 2):
        tmp = 0
        for i in m_mode2_count:
            tmp = tmp + i
        print("合计线程数：" + str(thead_count) + "，合计运行次数：" + str(tmp) + "，合计运行时间：" + str(m_max) + "秒，总TPS为：" + str(float(tmp) / float(m_max)))
    else:
        pass
