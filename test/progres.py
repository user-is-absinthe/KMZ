import sys
import time


def progress(count, total, status):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('%s: [%s] %s%s\r' % (status, bar, percents, '%'))
    sys.stdout.flush()


if __name__ == '__main__':
    total = 1000
    i = 0
    while i < total:
        progress(i, total, status='Doing very long job')
        time.sleep(0.5)  # emulating long-playing job
        i += 1
