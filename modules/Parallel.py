import time
import threading
import multiprocessing as mp
from modules.Quicksort import QuickSort
import os

class ParallelSort:
    def __init__(self, name_dict : dict):
        self.name_dict = name_dict
        
    def initialize_threads(self):
        # declare threads that can be used.
        try:
            thread_pool = mp.Pool(mp.cpu_count())
        except Exception as e:
            self.close_threads(thread_pool)
            print("Error creating threads: " + str(e))
            os.close()
        self.thread_pool = thread_pool
        return self.thread_pool

    def close_threads(self, thread_pool):
        thread_pool.close()

    def sort_names(self, thread_pool):
        quick_class = QuickSort(self.name_dict, 1, thread_pool)

        self.nd = self.name_dict

        quick_class.quicksort(0,len(self.nd)-1, 'last')
        init = 0
        high = -1

        while init < len(self.nd)-1:
            high = quick_class.count_groups(init,len(self.nd)-1)
            if high is None:
                break
            elif high[0] > 0:
                quick_class.quicksort(init, init+high[0], 'first')
                init=high[1]
            elif high[0] == 0:
                init = high[1]

        # added a return to pass the data back to ParallelSort class
        return self.nd
