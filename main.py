from modules.FileData import get_file_data
from modules.Parallel import ParallelSort
from modules.Sequential import SequentialSort
from multiprocessing import freeze_support

import time

if __name__ == '__main__':
    # Name file to import 
    FILE = 'files/names.txt'
    
    # Import file names as DICT {Key: {'first': <value>,'last':<value>}}
    name_dict = get_file_data(FILE)


    # Sequential runtime
    seq = SequentialSort(name_dict)

    start_seq_sort = time.time()
    seq_result = seq.sort_names()
    end_seq_sort = time.time()
    print("Total Time for Sequential: " + str(end_seq_sort - start_seq_sort))

    # reset to a clean DICT for parallel processing
    name_dict = get_file_data(FILE)

    # Parallel runtime
    par = ParallelSort(name_dict)
    # thread initialization not required in time counting
    par.initialize_threads()

    start_par_sort = time.time()
    par_result = par.sort_names()
    end_par_sort = time.time()
    print("Total Time for Parallel: " + str(end_par_sort - start_par_sort))
