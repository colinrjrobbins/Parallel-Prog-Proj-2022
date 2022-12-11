import time
import threading
import multiprocessing as mp
from modules.Sequential import SequentialSort as Seq
import os

class ParallelSortTwo:
    def __init__(self, name_dict : dict):
        self.name_dict = name_dict
        self.seq_class = Seq(name_dict)


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

    def partition(self, low: int, high: int, firstLast: str):
        pivot = self.nd[high][firstLast]

        i = low - 1

        for j in range(low, high):
            if self.nd[j][firstLast] <= pivot:
                i = i + 1
                (self.nd[i],self.nd[j]) = (self.nd[j], self.nd[i])

        (self.nd[i+1],self.nd[high]) = (self.nd[high],self.nd[i+1])

        return i + 1

    def quicksort(self, low: int, high: int, firstLast: str):
        if low < high:
            part = self.partition(low, high, firstLast)

            self.thread_pool.apply_async(self.quicksort, (low, part - 1, firstLast))

            self.thread_pool.apply_async(self.quicksort(part+1, high, firstLast))

    def count_groups(self, low: int, high: int):
        group_size = 0

        for j in range(low,high):
            if self.nd[j]['last'] == self.nd[j+1]['last']:
                group_size+=1
            elif group_size > 0:
                return [group_size, j+1]
            elif low:
                pass

    def sort_names(self, portion_dict = None):
        # Added portion in to be able to pass in smaller portions of code, None by default
        if portion_dict != None:
            self.nd = portion_dict
        else:
            pass

        self.nd = self.name_dict

        self.quicksort(0,len(self.nd)-1, 'last')
        init = 0
        high = -1

        while init < len(self.nd)-1:
            high = self.count_groups(init,len(self.nd)-1)
            if high is None:
                break
            elif high[0] > 0:
                self.quicksort(init, init+high[0], 'first')
                init=high[1]
            elif high[0] == 0:
                init = high[1]

        # added a return to pass the data back to ParallelSort class
        return self.nd

