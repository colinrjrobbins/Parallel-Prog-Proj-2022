import multiprocessing as mp
import os

class QuickSort:
    def __init__(self, name_dict: dict, parallelOrSequential: int, thread_pool = None) -> None:
        '''Quicksort class, name_dict in, parallelOrSequential, 1 = parallel, 0 = sequential'''
        self.nd = name_dict    
        self.PorS = parallelOrSequential
        self.thread_pool = thread_pool

    def partition(self, low: int, high: int, firstLast: str):
        pivot = self.nd[high][firstLast]

        i = low - 1

        for j in range(low, high):
            if self.nd[j][firstLast] <= pivot:
                i = i + 1
                (self.nd[i],self.nd[j]) = (self.nd[j], self.nd[i])

        (self.nd[i+1],self.nd[high]) = (self.nd[high],self.nd[i+1])

        return i + 1

    def quicksort(self, low: int, high:int, firstLast: str):
        if low < high:
            part = self.partition(low, high, firstLast)
            if self.PorS == 0:
                self.quicksort(low, part-1, firstLast)
                self.quicksort(part+1, high, firstLast)
            else:
                self.thread_pool.apply_async(self.quicksort, (low, part - 1, firstLast))
                self.thread_pool.apply_async(self.quicksort, (part+1, high, firstLast))

    def count_groups(self, low: int, high: int):
        group_size = 0

        for j in range(low,high):
            if self.nd[j]['last'] == self.nd[j+1]['last']:
                group_size+=1
            elif group_size > 0:
                return [group_size, j+1]
            elif low:
                pass