def get_file_data(filename : str):
    """ Function: used to open and convert the file into a python dict and return data """
    name_file = open(filename, 'r')

    # Open the file and split the data by new lines.
    file_data = name_file.read()
    file_string = file_data.split('\n')
    name_dict = {}

    # Initialize X as a key counter
    x = 0

    # Loop through and assign first and last name to each key
    for name in file_string:
        name_dict[x] = {"first":name.split(' ')[0],"last":name.split(' ')[1]}
        x = x + 1

    name_file.close()

    return name_dict