from modules.FileData import get_file_data
from modules.Parallel import ParallelSort
from modules.Sequential import SequentialSort
import time

# Name file to import 
FILE = 'files/names.txt'
 
# example to test time (not necessary for the project but a good example)
start_import = time.time()
name_dict = get_file_data(FILE)
end_import = time.time()
print("Total File Import Time: " + str(end_import - start_import))

# Sequential runtime
seq = SequentialSort(name_dict)

start_seq_sort = time.time()
seq.sort_names()
end_seq_sort = time.time()
print("Total Time for Sequential: " + str(end_seq_sort - start_seq_sort))

# Parallel runtime
par = ParallelSort(name_dict)
# thread initialization not required in time counting
par.initialize_threads()

start_par_sort = time.time()
par.sort_names()
end_par_sort = time.time()
print("Total Time for Parallel: " + str(end_par_sort - start_par_sort))