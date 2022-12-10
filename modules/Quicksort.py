import multiprocessing as mp
import os

class QuickSort:
    def __init__(self, name_dict: dict, parallelOrSequential: int, thread_pool = None) -> None:
        '''Quicksort class, name_dict in, parallelOrSequential, 1 = parallel, 0 = sequential'''
        self.nd = name_dict    
        self.PorS = parallelOrSequential
        self.thread_pool = thread_pool
        self.lock = mp.Lock()
        self.firstLast = "last"

    def switch_parallel_sequential(self):
        if self.PorS == 0:
            self.PorS = 1
        else:
            self.PorS = 0

    def update_first_last(self):
        if self.firstLast == "last":
            self.firstLast = "first"
        else:
            self.firstLast = "last"

    def update_thread_pool(self, thread_object):
        self.thread_pool = thread_object

    def partition(self, low: int, high: int):
        pivot = self.nd[high][self.firstLast]

        i = low - 1
        for j in range(low, high):
            if self.nd[j][self.firstLast] <= pivot:
                i = i + 1
                (self.nd[i],self.nd[j]) = (self.nd[j], self.nd[i])
                
        (self.nd[i+1],self.nd[high]) = (self.nd[high],self.nd[i+1])

        return i + 1

    def parallel_partition(self, low: int, high: int):
        pivot = self.nd[high][self.firstLast]
        i = low - 1
        for j in range(low, high):
            if self.nd[j][self.firstLast] <= pivot:
                i = i + 1
                with self.lock:
                    (self.nd[i],self.nd[j]) = (self.nd[j], self.nd[i])
        with self.lock:
            (self.nd[i+1],self.nd[high]) = (self.nd[high],self.nd[i+1])
        
        return i + 1

    def quicksort(self, low: int, high:int):
        if low < high:
            if self.PorS == 0:
                part = self.partition(low, high)
            else:
                part = self.parallel_partition(low, high)

            if self.PorS == 0:
                self.quicksort(low, part-1)
                self.quicksort(part+1, high)
            else:
                try:
                    self.thread_pool.map(self.quicksort, [(low, part - 1),(part+1,high)])
                    #self.thread_pool.submit(self.quicksort, (part+1, high))
                except Exception as e:
                    print("Error called: QuickSort Class : quicksort Method : " + str(e))
                    print("Closing threads.")
                    self.thread_pool.shutdown()

    def count_groups(self, low: int, high: int):
        group_size = 0
        with self.lock:
            if self.PorS == 0:
                for j in range(low,high):
                    if self.nd[j]['last'] == self.nd[j+1]['last']:
                        group_size = group_size + 1
                    elif group_size > 0:
                        return [group_size, j+1]
                    elif low:
                        pass
            else:
                for j in range(low,high):
                    if self.nd[j][self.firstLast] == self.nd[j+1][self.firstLast]:#if self.nd[j]['last'] == self.nd[j+1]['last']:
                        group_size = group_size + 1
                    elif group_size > 0:
                        return [group_size, j+1]
                    elif low:
                        pass