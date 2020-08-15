# https://stackoverflow.com/questions/63426621/question-about-python-thread-modules-lock
import sys
import thread
a = 1
lock = thread.allocate_lock()
def abc(lock, x):
    print "1 %d" % x
    lock.acquire()
    a = 5
    lock.release()
    sys.stdout.flush()
for x in range(0, 10):
    thread.start_new_thread(abc, (lock, x))
