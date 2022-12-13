from modules.FileData import get_file_data
from modules.Parallel import ParallelSort
from modules.Sequential import SequentialSort

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

    seq_time = end_seq_sort - start_seq_sort

    print("Total Time for Sequential: " + str(seq_time))

    seq_file = open('files/sequential_names_sorted.txt','w')
    for x in range(0,len(seq_result)):
        seq_file.write(seq_result[x]['first'] + ' ' + seq_result[x]['last'] + '\n')
    seq_file.close()

    # ============ PARALLEL DEVELOPMENT ==============

    # reset to a clean DICT for parallel processing
    name_dict = get_file_data(FILE)

    # Parallel runtime
    par = ParallelSort(name_dict)
    # thread initialization not required in time counting
    thread_pool = par.initialize_threads()

    start_par_sort = time.time()
    par_result = par.sort_names(thread_pool)
    end_par_sort = time.time()

    par_time = end_par_sort - start_par_sort

    print("Total Time for Parallel: " + str(par_time))
    
    par_file = open('files/parallel_names_sorted.txt','w')
    for x in range(0,len(par_result)):
        par_file.write(par_result[x]['first'] + ' ' + par_result[x]['last'] + '\n')
    par_file.close()

    # ======= DETERMINE TOTAL SPEED DIFFERENCE ===========

    if seq_time > par_time:
        lapse = seq_time / par_time
        print("\nParallel is ~" + str(round(lapse, 2)) + "x faster.")
    else:
        lapse = par_time / seq_time
        print("\nSequential is ~" + str(round(lapse, 2)) + "x faster.")
    
    # ====== OPEN AND READ FILES FOR COMPARISON ===========

    seq_file_data = open('files/sequential_names_sorted.txt','r').readlines()
    par_file_data = open('files/parallel_names_sorted.txt','r').readlines()

    seq_list = []
    par_list = []

    for name in seq_file_data:
        seq_list.append(name.split('\n')[0])

    for name in par_file_data:
        par_list.append(name.split('\n')[0])

    for x in range(0,len(seq_list)):
        line1 = seq_list[x]
        line2 = par_list[x]
        if line1 != line2:
            nomatch = 1
            break
        else:
            nomatch = 0

    if nomatch == 1:
        print("\nFiles do not match.\n")
    else:
        print("\nFiles match.\n")