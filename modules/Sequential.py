import time
import multiprocessing as mp
from modules.Quicksort import QuickSort

class SequentialSort:
    def __init__(self, name_dict : dict):
        self.nd = name_dict

    def sort_names(self):
        quick_class = QuickSort(self.nd, 0)

        quick_class.quicksort(0,len(self.nd)-1, 'last')
        init = 0
        high = -1
        #return self.nd

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

