# This is a backend project for shop website with Postgresql
import DataBaseService as DBS
import FrontCommunication as FBS
from threading import Thread


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # create two new threads
    t1 = Thread(target=FBS.initServer)
    t2 = Thread(target=DBS.initDBLoop)
    # start the threads
    t1.start()
    t2.start()
    # wait for the threads to complete
    t1.join()
    t2.join()


