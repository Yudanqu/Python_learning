import time
def consumer(name):
    print("%s ׼���԰���" %name)
    while True:
        baozi = yield

        print("����[%s]���ˣ���[%s]����" %(baozi,name))

def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print("���ӿ�ʼ��������")
    for i in range(10):
        time.sleep(1)
        print("����2������")
        c.send(i)
        c2.send(i)

producer("alex")