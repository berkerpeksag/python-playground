# Based on https://www.metachris.com/2016/04/python-threadpool/

import queue
import threading
import traceback


class Worker(threading.Thread):

    def __init__(self, tasks):
        super().__init__(daemon=True)
        self.tasks = tasks
        self.start()

    def run(self):
        while True:
            func, args, kwargs = self.tasks.get()
            try:
                func(*args, **kwargs)
            except Exception:
                # An exception happened in this thread
                traceback.print_exc()
            finally:
                # Mark this task as done, whether an exception happened or not
                self.tasks.task_done()


class ThreadPool:

    def __init__(self, num_threads):
        self.tasks = queue.Queue(num_threads)
        for _ in range(num_threads):
            Worker(self.tasks)

    def add_task(self, func, *args, **kargs):
        self.tasks.put((func, args, kargs))

    def map(self, func, args_list):
        for args in args_list:
            self.add_task(func, args)

    def wait_completion(self):
        self.tasks.join()


if __name__ == '__main__':
    import random
    import time

    def wait_delay(delay):
        print('[%d] sleeping for %d sec' % (time.time(), delay))
        time.sleep(delay)

    delays = [random.randrange(3, 7) for i in range(50)]

    pool = ThreadPool(5)

    # Add the jobs in bulk to the thread pool.  Alternatively you could use
    # pool.add_task() to add single jobs.  The code will block here, which
    # makes it possible to cancel the thread pool with an exception when
    # the currently running batch of workers is finished.
    pool.map(wait_delay, delays)
    pool.wait_completion()
