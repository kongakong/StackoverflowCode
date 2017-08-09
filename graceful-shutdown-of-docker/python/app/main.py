import signal
import os
import time


def receive_signal(signum, stack):
    print 'Received:', signum

signal.signal(signal.SIGTERM, receive_signal)
# python cannot handle KILL
# signal.signal(signal.SIGKILL, receive_signal)


def main():
    print "Waiting signal"
    signal.pause()


if __name__ == '__main__':
    main()

