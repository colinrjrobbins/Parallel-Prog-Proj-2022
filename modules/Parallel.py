import time
import threading
import multiprocessing as mp
from multiprocessing.pool import ThreadPool
from modules.Quicksort import QuickSort
import os

class ParallelSort:
    def __init__(self, name_dict : dict):
        self.name_dict = name_dict
        self.quick_class = QuickSort(self.name_dict,1)
        self.lock = mp.Lock()
        self.length = len(self.name_dict)-1
        
    def initialize_threads(self):
        # declare threads that can be used.
        try:
            thread_pool = ThreadPool(mp.cpu_count())
        except Exception as e:
            self.close_threads(thread_pool)
            print("Error creating threads: " + str(e))
            os.close()
        self.thread_pool = thread_pool
        return self.thread_pool

    def close_threads(self, thread_pool):
        thread_pool.close()
        thread_pool.join()
        
    def sort_names(self, thread_pool):
        self.quick_class.update_thread_pool(thread_pool)
        with self.lock:
            self.quick_class.quicksort(0, self.length, 'last')

        init = 0
        high = -1

        self.quick_class.switch_parallel_sequential()
        while init < len(self.name_dict)-1:
            with self.lock:
                high = thread_pool.apply(self.quick_class.count_groups,(init, self.length))#.get()
            if high is None:
                break
            elif high[0] > 0:
                with self.lock:
                    self.quick_class.quicksort(init, init+high[0], 'first')
                    init=high[1]
            elif high[0] == 0:
                print(str(init))
                init = high[1]

        # added a return to pass the data back to ParallelSort class
        return self.name_dict
