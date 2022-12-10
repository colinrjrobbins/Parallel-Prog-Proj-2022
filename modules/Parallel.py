import time
import threading
import multiprocessing as mp
from concurrent.futures import ThreadPoolExecutor
from multiprocessing.pool import ThreadPool
from modules.Quicksort import QuickSort
import os

# class ParallelSort:
#     def __init__(self, name_dict : dict):
#         self.name_dict = name_dict
#         self.quick_class = QuickSort(self.name_dict,1)
#         self.lock = mp.Lock()
        
#     def initialize_threads(self):
#         # declare threads that can be used.
#         try:
#             thread_pool = ThreadPool(mp.cpu_count())
#         except Exception as e:
#             self.close_threads(thread_pool)
#             print("Error creating threads: " + str(e))
#             os.close()
#         self.thread_pool = thread_pool
#         return self.thread_pool

#     def close_threads(self, thread_pool):
#         thread_pool.close()

#     # def last_name_count(self,name_dict : dict):
#     #     '''last_name_count: take in last name sorted and count distinct names'''
#     #     name_count = []
#     #     for name in range(0,len(self.name_dict)):
#     #         count = 0

#     #         for x in range(0, len(self.name_dict)):


#     def sort_names(self, thread_pool):
#         # Attempted starting with sequential

#         #self.quick_class.switch_parallel_sequential()

#         self.quick_class.update_thread_pool(thread_pool)
#         self.quick_class.quicksort(0, len(self.name_dict)-1, 'last')
        
#         init = 0
#         high = -1

#         # switch from sequential to parallel
        

        
#         while init < len(self.name_dict)-1:
#             #self.quick_class.switch_parallel_sequential()
#             high = self.quick_class.count_groups(init, len(self.name_dict)-1)
#             if high is None:
#                 break
#             elif high[0] > 0:
#                 self.quick_class.quicksort(init, init+high[0], 'first')
#                 init=high[1]
#             elif high[0] == 0:
#                 print(str(init))
#                 init = high[1]

#         # added a return to pass the data back to ParallelSort class
#         return self.name_dict

class ParallelSort:
    def __init__(self, names_dict: dict):
        self.names_dict = names_dict
        self.quick_class = QuickSort(self.names_dict, 1)
        self.lock = mp.Lock()

    def initialize_threads(self):
        try:
            # with ThreadPool(processes=mp.cpu_count()) as thread_pool:
            #     self.thread_pool = thread_pool
            #     return self.thread_pool
            thread_pool = ThreadPoolExecutor(max_workers=mp.cpu_count())
        except Exception as e:
            print("Error creating threads: " + str(e))
            os.close()
        self.thread_pool = thread_pool
        return self.thread_pool

    def shutdown_thread_pool(self):
        self.thread_pool.shutdown()

    def sort_names(self, thread_pool):
        self.quick_class.update_thread_pool(thread_pool)

        with self.lock:
            self.quick_class.quicksort(0, len(self.names_dict)-1)
        
        self.quick_class.update_first_last()

        init = 0
        high = -1

        while init < len(self.names_dict)-1:
            high = self.quick_class.count_groups(init, len(self.names_dict)-1)
            if high is None:
                break
            elif high[0] > 0:
                self.quick_class.quicksort(init, init+high[0])
                init = high[1]
            elif high[0] == 0:
                init = high[1]

        self.shutdown_thread_pool()

        return self.names_dict

