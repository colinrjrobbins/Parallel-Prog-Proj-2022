import multiprocessing as mp
import os

class QuickSort:
    def __init__(self, name_dict: dict, parallelOrSequential: int, thread_pool = None) -> None:
        '''Quicksort class, name_dict in, parallelOrSequential, 1 = parallel, 0 = sequential'''
        self.nd = name_dict    
        self.PorS = parallelOrSequential
        self.thread_pool = thread_pool
        self.lock = mp.Lock()

    def switch_parallel_sequential(self):
        '''Used to switch between sequential and parallel implementation mid run.'''
        if self.PorS == 0:
            self.PorS = 1
        else:
            self.PorS = 0

    def update_thread_pool(self, thread_object):
        '''Update the threadpool anywhere. (req: thread_pool Object)'''
        self.thread_pool = thread_object

    def partition(self, low: int, high: int, firstLast: str):
        '''Take the high and low, as well as the sort identifier (first name or last name) and switch based on alphebetical response.'''
        pivot = self.nd[high][firstLast]

        i = low - 1
        for j in range(low, high):
            if self.nd[j][firstLast] <= pivot:
                i = i + 1
                (self.nd[i],self.nd[j]) = (self.nd[j], self.nd[i])

        (self.nd[i+1],self.nd[high]) = (self.nd[high],self.nd[i+1])

        return i + 1

    def quicksort(self, low: int, high:int, firstLast: str):
        '''Quicksort method, determine partition amount and split based on whether parallel or sequential initialization'''
        if low < high:
            part = self.partition(low, high, firstLast)
            if self.PorS == 0:
                self.quicksort(low, part-1, firstLast)
                self.quicksort(part+1, high, firstLast)
            else:
                try:
                    self.thread_pool.apply_async(self.quicksort, (low, part - 1, firstLast))
                    self.thread_pool.apply_async(self.quicksort, (part+1, high, firstLast))
                except Exception as e:
                    print("Error called: QuickSort Class : quicksort Method : " + str(e))
                    print("Closing threads.")
                    self.thread_pool.close()

    def count_groups(self, low: int, high: int):
        '''Count the last name groups and return the size of the group to sort by first name.'''
        group_size = 0
        for j in range(low,high):
            if self.nd[j]['last'] == self.nd[j+1]['last']:
                with self.lock:
                    group_size = group_size + 1
            elif group_size > 0:
                return [group_size, j+1]
            elif low:
                pass