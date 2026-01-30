import threading,time

def reservation(nos):
    global totnos
    obj.acquire()
    if(nos>totnos):
        print("\t Hii {} ,{} seats are not avialable !Try again".format(threading.current_thread().name,nos))
    else:

        totnos=totnos-nos
        print("{} seats are reserved ...Happy journy".format(totnos))
        time.sleep(2)
        print("Number of seats available",totnos)
        time.sleep(2)
        if(totnos==0):
            print("Train is full")

    obj.release()
obj=threading.Lock()
totnos=20
t=threading.Thread(target=reservation,args=(10,))
t1=threading.Thread(target=reservation,args=(33,))
t2=threading.Thread(target=reservation,args=(2,))
t3=threading.Thread(target=reservation,args=(4,))
t.start()
t1.start()
t2.start()
t3.start()
t1.join()
t1.join()
t2.join()
t3.join()

