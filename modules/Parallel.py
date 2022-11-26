import time
import threading
import multiprocessing as mp
from modules.Sequential import SequentialSort as Seq
import os

class ParallelSort:
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

    def sort_names(self):
        try:
            # grab threads that have been initialized in main.py
            thread_pool = self.thread_pool
            split_dict = int(mp.cpu_count())

            initial = 0
            # Split dict evenly by number of cores
            dict_split_length = (round(len(self.name_dict) / split_dict))

            portions = []
            temp_holder = []

            # create portions based on the split size
            for y in range(split_dict):
                for x in range(initial, dict_split_length):
                    temp_holder.append(self.name_dict[x])
                    initial = dict_split_length
                    dict_split_length = dict_split_length + dict_split_length
                    if dict_split_length > len(self.name_dict):
                        dict_split_length = len(self.name_dict)
                portions.append(temp_holder)

        except Exception as e:
            print("Issue in thread creation: " + str(e))
            self.close_threads(thread_pool)
            input()
            os.close()

        try:
            # run quicksort on each individual thread
            result = thread_pool.map(self.seq_class.sort_names, [item for item in portions])
        except Exception as e:
            print("Error: " + str(e))
            self.close_threads(thread_pool)
            input()
            os.close()

        # NEED TO WORK ON THIS PART
        # Merges all the dictonaries back together into one
        new_name_dict = {}
        for x in range(0, len(result)):
            new_name_dict.update(result[x])

        # runs a quicksort on the final dict to do a final sort.
        final_par_dict = self.seq_class.sort_names(new_name_dict)

        return final_par_dict
