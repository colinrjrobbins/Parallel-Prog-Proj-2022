import time

class SequentialSort:
    def __init__(self, name_dict : dict):
        self.nd = name_dict

    def partition(self, low: int, high: int, firstLast: str):
        pivot = self.nd[high][firstLast]

        if firstLast == 'last':
            lastFirst = 'first'

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

            self.quicksort(low, part - 1, firstLast)

            self.quicksort(part+1, high, firstLast)

    def sort_names(self):
        print("\nSHOWING TOP 10 FROM FILE")
        for i in range(0,10):
            print(self.nd[i]['first'] + ' ' + self.nd[i]['last'])

        input("\nPress enter to sort...")

        self.quicksort(0,len(self.nd)-1, 'last')
        #self.quicksort(0,len(self.nd)-1, 'first')

        print("\nSHOWING TOP 10 FROM SORT")
        for i in range(0,10):
            print(self.nd[i]['first'] + ' ' + self.nd[i]['last'])