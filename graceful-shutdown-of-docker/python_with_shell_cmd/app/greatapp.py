import os
import time
import logging
import signal


LOG_FORMAT = "%(asctime)-15s pid %(process)d tid %(thread)4d %(levelname)-8s" \
    " %(module)-8s %(message)s"

logging.basicConfig(format=LOG_FORMAT)
LOG = logging.getLogger(__file__)
LOG.setLevel(logging.DEBUG)

def docker_shutdown_handler(_signum, _frame):
    LOG.info("Handling shutdown...%s", _signum)
    # sys.exit()


LOG.info('Registering signal handler')
signal.signal(signal.SIGTERM, docker_shutdown_handler)
signal.signal(signal.SIGUSR1, docker_shutdown_handler)


def main():
    LOG.info("Hello!")
    sleep_time = 2
    while True:
        time.sleep(sleep_time)
        LOG.info("Checking every %ds...", sleep_time)


if __name__ == '__main__':
    main()
