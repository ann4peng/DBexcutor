import threading
from threading import Thread

from RockModels import MeterData


def method(s):
    s = str(s)
    s += "OhHaHa"
    print  '--------- ' + threading.current_thread().getName()
    print s



# method(a)

def createThread(name='default'):
    th = Thread(target=method, args=['jiejie'])
    th.setName(name)
    # th.setDaemon(True)
    return th


createThread().start()
createThread('OhHaHaThread').start()


print MeterData()
print ','.join(['?' for i in range(0, 5)])
